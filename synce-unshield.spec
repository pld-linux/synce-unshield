--- synce-unshield.spec	2005-10-29 22:48:15.000000000 +0200
+++ /home/users/prism/tmp/adapter-9T9FXe/synce-unshield.spec	2005-10-29 22:48:46.000000000 +0200
@@ -1,3 +1,4 @@
+# $Revision: 1.1 $, $Date: 2005-10-29 20:50:50 $
 %define	_realname	unshield
 
 Summary:	SynCE Unshield - a tool to extract the InstallShield Cabinet Files
@@ -7,7 +8,7 @@
 Release:	1
 License:	MIT
 Group:		Applications
-Source0: 	http://dl.sourceforge.net/synce/%{_realname}-%{version}.tar.gz
+Source0:	http://dl.sourceforge.net/synce/%{_realname}-%{version}.tar.gz
 # Source0-md5:	ff6bb0fbe962bc00e230592c910b90ce
 URL:		http://synce.sourceforge.net/
 BuildRequires:	autoconf >= 2.50
@@ -19,19 +20,19 @@
 BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
 
 %description
-An installer created by the InstallShield software stores the files
-it will install inside of InstallShield Cabinet Files. It would thus
-be desirable to be able to extract the Microsoft Cabinet Files from
-the InstallShield Cabinet Files in order to be able to install the
-applications without access to Microsoft Windows. Unshield is a solution
-that allows to perform this task.
+An installer created by the InstallShield software stores the files it
+will install inside of InstallShield Cabinet Files. It would thus be
+desirable to be able to extract the Microsoft Cabinet Files from the
+InstallShield Cabinet Files in order to be able to install the
+applications without access to Microsoft Windows. Unshield is a
+solution that allows to perform this task.
 
 %description -l pl
-Instalator stworzony przez oprogramowanie InstallShield przechowuje pliki
-do zainstalowania wewn±trz plików InstallShield Cabinet. Jest po¿±dane, 
-by da³o siê rozpakowaæ zawarto¶æ plików InstallShield Cabinet w celu
-instalacji aplikacji bez dostêpu do Microsoft Windows. Unshield jest narzêdziem
-stworzonym do tego celu.
+Instalator stworzony przez oprogramowanie InstallShield przechowuje
+pliki do zainstalowania wewn±trz plików InstallShield Cabinet. Jest
+po¿±dane, by da³o siê rozpakowaæ zawarto¶æ plików InstallShield
+Cabinet w celu instalacji aplikacji bez dostêpu do Microsoft Windows.
+Unshield jest narzêdziem stworzonym do tego celu.
 
 %package libs
 Summary:	The Unshield library
@@ -98,6 +99,7 @@
 %attr(755,root,root) %{_bindir}/*
 
 %files libs
+%defattr(644,root,root,755)
 %attr(755,root,root) %{_libdir}/libunshield.so.*.*.*
 
 %files libs-devel
