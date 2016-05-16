install:
	mkdir -p ${DESTDIR}/usr/bin
	mkdir -p ${DESTDIR}/usr/share/mkws
	cp -r mkws/templates/ ${DESTDIR}/usr/share/mkws/
	cp mkws/cli.py ${DESTDIR}/usr/bin/mkws

uninstall:
	rm -r ${DESTDIR}/usr/share/mkws
	rm ${DESTDIR}/usr/bin/mkws
