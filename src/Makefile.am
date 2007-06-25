
bin_PROGRAMS = policyd cleanup stats


policyd_SOURCES = policyd.c syslog.c generic.c mysql.c greylist.c throttle.c 
policyd_SOURCES += sockets.c cidr.c spamtrap.c blacklist.c blacklist_helo.c
policyd_SOURCES += whitelist.c throttle_host.c throttle_sasl.c throttle_from.c
policyd_SOURCES += throttle_rcpt.c helo.c
policyd_LDFLAGS = @LIBMYSQLCLIENT@
policyd_CFLAGS = @MYSQL_INCLUDE@ $(AM_CFLAGS)

cleanup_SOURCES = cleanup.c syslog.c cidr.c generic.c sockets.c mysql.c
cleanup_LDFLAGS = @LIBMYSQLCLIENT@
cleanup_CFLAGS = @MYSQL_INCLUDE@ $(AM_CFLAGS)

stats_SOURCES = stats.c cidr.c syslog.c generic.c sockets.c mysql.c
stats_LDFLAGS = @LIBMYSQLCLIENT@
stats_CFLAGS = @MYSQL_INCLUDE@ $(AM_CFLAGS)

