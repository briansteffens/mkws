install:
	mkdir -p ${DESTDIR}/usr/bin
	ln -s `pwd`/mkws/cli.py ${DESTDIR}/usr/bin/mkws
