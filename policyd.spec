%define ver 1.82
%define rel 1
%define _vendor redhat

%define release %(release="`rpm -q --queryformat='.%{VERSION}' redhat-release 2>/dev/null`";if test $? = 0;then release=".rhl.`echo $release|cut -d. -f2`";else if test $? != 0;then release="`rpm -q --queryformat='.%{VERSION}' fedora-release 2>/dev/null`";if test $? = 0;then release=".fc`echo $release|cut -d. -f2`";else if test $? != 0;then release="`rpm -q --queryformat='.%{VERSION}' centos-release 2>/dev/null`";if test $? = 0;then release="rhl`echo $release|cut -d. -f2`"; else release="";fi;fi;fi;fi;fi;if [ "$release" == ".rhl.5Server" ]; then release=.rhl5;fi;echo $release)

Summary:		Postfix Policyd Daemon
Name:			policyd
Version:		%{ver}
Release:		%{rel}%{release}
URL:			http://%{name}.sourceforge.net/
Source0:		http://%{name}.sourceforge.net/%{name}-%{ver}.tar.gz
License:		GNU GPL v2
Group:			System/Daemons
BuildRoot:		%{_tmppath}/%{name}-%{version}-root
BuildRequires:		gcc
Requires:		postfix >= 2.1 mysql >= 3 mysql-server >= 3

%description
Policyd is a policy server for Postfix (written in C) that enables
advanced Greylisting with many other anti-spam facilities. See the
docs and policyd.conf for features that are ever being augmented. 
It needs MySQL v3 or greater and is currently only certified for
MySQL v4.

%prep

%setup -q

%build
make build

%install
rm -rf $RPM_BUILD_ROOT

# Misc stuff
sed -i 's|PROG=\"/usr/local/%{name}/%{name}\"|PROG=\"%{_sbindir}/%{name}\"|' contrib/%{name}.%{_vendor}.init
sed -i 's|CONF=\"/usr/local/%{name}/%{name}.conf\"|CONF=\"%{_sysconfdir}/%{name}.conf\"|' contrib/%{name}.%{_vendor}.init
sed -i 's|/usr/local/%{name}/cleanup|%{_sbindir}/cleanup|' contrib/%{name}.cron
sed -i 's|/usr/local/%{name}/%{name}.conf|%{_sysconfdir}/%{name}.conf|' contrib/%{name}.cron
install -d $RPM_BUILD_ROOT%{_sysconfdir}/postfix
install -d $RPM_BUILD_ROOT%{_sysconfdir}/rc.d/init.d
install -d $RPM_BUILD_ROOT%{_sysconfdir}/cron.d
install -d $RPM_BUILD_ROOT%{_sbindir}
install -d $RPM_BUILD_ROOT%{_sysconfdir}/cron.d
install -p -m755 contrib/%{name}.%{_vendor}.init $RPM_BUILD_ROOT/%{_sysconfdir}/rc.d/init.d/%{name}
install -p -m644 contrib/%{name}.cron $RPM_BUILD_ROOT%{_sysconfdir}/cron.d/%{name}
install -p -m755 %{name} $RPM_BUILD_ROOT%{_sbindir}
install -p -m755 cleanup $RPM_BUILD_ROOT%{_sbindir}/cleanup
install -p -m755 stats $RPM_BUILD_ROOT%{_sbindir}
install -p -m600 %{name}.conf $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.conf
install -p -m644 contrib/%{name}.cron $RPM_BUILD_ROOT/etc/cron.d/%{name}
install -p -m600 %{name}.conf $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}.conf

%post
/sbin/chkconfig --add %{name}

%postun
/sbin/service %{name} condrestart > /dev/null 2>&1 || :

%preun
if [ "$1" = 0 ]
then
	/sbin/service %{name} stop > /dev/null 2>&1 || :
	/sbin/chkconfig --del %{name}

%files
%defattr(-,root,root)
%doc %attr(-,root,root) ChangeLog DATABASE.mysql LICENSE README TODO doc/*
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/%{name}.conf
%attr(0755,root,root) %config(noreplace) %{_sysconfdir}/rc.d/init.d/%{name}
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/cron.d/%{name}
%attr(0755,root,root) %{_sbindir}/%{name}
%attr(0755,root,root) %{_sbindir}/cleanup
%attr(0755,root,root) %{_sbindir}/stats

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%changelog
* Sat Sep 1 2007 Tonni Earnshaw <tonni@hetnet.nl>
- Completely revamped so that the spec will build on Red Hat or Fedora.
- Removed previous OS dependency.

* Tue Mar 14 2006 Tony Earnshaw <tonni@barlaeus.nl>
- Red Hat RHAS/RHEL adaptation
