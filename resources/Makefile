# requires PyQt5 installed
#
all: errordlg.py startdlg.py traitchooserdlg.py mainwindow.py

errordlg.py : errordlg.ui
	pyuic5 errordlg.ui -o errordlg.py 

startdlg.py : startdlg.ui
	pyuic5 startdlg.ui -o startdlg.py 

traitchooserdlg.py : traitchooserdlg.ui
	pyuic5 traitchooserdlg.ui -o traitchooserdlg.py 

mainwindow.py : mainwindow.ui
	pyuic5 mainwindow.ui -o mainwindow.py 

		
clean:
	rm errordlg.py
	rm startdlg.py
	rm traitchooserdlg.py
	rm mainwindow.py
