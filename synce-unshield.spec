Summary:	SynCE Unshield - a tool to extract InstallShield Cabinet files
Summary(pl.UTF-8):	SynCE Unshield - narzędzie do rozpakowywania archiwów InstallShield
Name:		synce-unshield
Version:	0.6
Release:	1
License:	MIT
Group:		Applications
Source0:	http://dl.sourceforge.net/synce/unshield-%{version}.tar.gz
# Source0-md5:	31a829192a255160d1f71cda4c865c9c
URL:		http://www.synce.org/
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

%description -l pl.UTF-8
Instalator stworzony przez oprogramowanie InstallShield przechowuje
pliki do zainstalowania wewnątrz plików InstallShield Cabinet. Jest
pożądane, by dało się rozpakować zawartość plików InstallShield
Cabinet w celu instalacji aplikacji bez dostępu do Microsoft Windows.
Unshield jest narzędziem stworzonym do tego celu.

%package libs
Summary:	The Unshield library
Summary(pl.UTF-8):	Biblioteka Unshield
Group:		Libraries

%description libs
The Unshield library.

%description libs -l pl.UTF-8
Biblioteka Unshield.

%package libs-devel
Summary:	Header files for the Unshield library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Unshield
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description libs-devel
Header files for the Unshield library.

%description libs-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Unshield.

%package libs-static
Summary:	Static Unshield library
Summary(pl.UTF-8):	Statyczna biblioteka Unshield
Group:		Development/Libraries
Requires:	%{name}-libs-devel = %{version}-%{release}

%description libs-static
Static Unshield library.

%description libs-static -l pl.UTF-8
Statyczna biblioteka Unshield.

%prep
%setup -q -n unshield-%{version}

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
%attr(755,root,root) %{_bindir}/unshield
%{_mandir}/man1/unshield.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libunshield.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libunshield.so.?

%files libs-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libunshield.so
%{_libdir}/libunshield.la
%{_includedir}/libunshield.h
%{_pkgconfigdir}/libunshield.pc

%files libs-static
%defattr(644,root,root,755)
%{_libdir}/libunshield.a
