
%define	_realname	unshield

Summary:	SynCE Unshield - a tool to extract InstallShield Cabinet files
Summary(pl):	SynCE Unshield - narzêdzie do rozpakowywania archiwów InstallShield
Name:		synce-%{_realname}
Version:	0.5
Release:	1
License:	MIT
Group:		Applications
Source0:	http://dl.sourceforge.net/synce/%{_realname}-%{version}.tar.gz
# Source0-md5:	ff6bb0fbe962bc00e230592c910b90ce
URL:		http://synce.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1.4
BuildRequires:	libtool
BuildRequires:	rpmbuild(macros) >= 1.213
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An installer created by the InstallShield software stores the files it
will install inside of InstallShield Cabinet Files. It would thus be
desirable to be able to extract the Microsoft Cabinet Files from the
InstallShield Cabinet Files in order to be able to install the
applications without access to Microsoft Windows. Unshield is a
solution that allows to perform this task.

%description -l pl
Instalator stworzony przez oprogramowanie InstallShield przechowuje
pliki do zainstalowania wewn±trz plików InstallShield Cabinet. Jest
po¿±dane, by da³o siê rozpakowaæ zawarto¶æ plików InstallShield
Cabinet w celu instalacji aplikacji bez dostêpu do Microsoft Windows.
Unshield jest narzêdziem stworzonym do tego celu.

%package libs
Summary:	The Unshield library
Summary(pl):	Biblioteka Unshield
Group:		Libraries

%description libs
The Unshield library.

%description libs -l pl
Biblioteka Unshield.

%package libs-devel
Summary:	Header files for the Unshield library
Summary(pl):	Pliki nag³ówkowe biblioteki Unshield
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description libs-devel
Header files for the Unshield library.

%description libs-devel -l pl
Pliki nag³ówkowe biblioteki Unshield.

%package libs-static
Summary:	Static Unshield library
Summary(pl):	Statyczna biblioteka Unshield
Group:		Development/Libraries
Requires:	%{name}-libs-devel = %{version}-%{release}

%description libs-static
Static Unshield library.

%description libs-static -l pl
Statyczna biblioteka Unshield.

%prep
%setup -q -n %{_realname}-%{version}

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE README* TODO
%attr(755,root,root) %{_bindir}/*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libunshield.so.*.*.*

%files libs-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libunshield.so
%{_libdir}/libunshield.la
%{_includedir}/libunshield.h
%{_aclocaldir}/unshield.m4

%files libs-static
%defattr(644,root,root,755)
%{_libdir}/libunshield.a
