Summary:	Interface library to the ICA device driver
Summary(pl.UTF-8):	Biblioteka interfejsu do sterownika urządzenia ICA
Name:		libica2
Version:	4.3.0
Release:	1
License:	CPL v1.0
Group:		Libraries
#Source0Download: https://github.com/opencryptoki/libica
Source0:	https://github.com/opencryptoki/libica/archive/v%{version}/libica-%{version}.tar.gz
# Source0-md5:	a197e95cd8af7e844954c11f99c1ba8a
Patch0:		%{name}-headers.patch
URL:		https://github.com/opencryptoki/libica
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.9.5
BuildRequires:	libtool >= 2:2
BuildRequires:	openssl-devel >= 1.1.1
Requires:	openssl >= 1.1.1
Provides:	libica = %{version}
Obsoletes:	libica < 2.0
ExclusiveArch:	s390 s390x
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Interface library routines used by IBM modules to interface to the IBM
eServer Cryptographic Accelerator (ICA).

%description -l pl.UTF-8
Biblioteka interfejsu używana przez moduły IBM-a do współpracy z
akceleratorem kryptograficznym IBM eServer Cryptographic Accelerator
(ICA).

%package devel
Summary:	Header files for ICA library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki ICA
Group:		Development/Libraries
Provides:	libica-devel = %{version}
Requires:	%{name} = %{version}-%{release}
Requires:	openssl-devel >= 1.1.1
Obsoletes:	libica-devel < 2.0

%description devel
Header files for ICA library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki ICA.

%package static
Summary:	Static ICA library
Summary(pl.UTF-8):	Statyczna biblioteka ICA
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Provides:	libica-static = %{version}
Obsoletes:	libica-static < 2.0

%description static
Static ICA library.

%description static -l pl.UTF-8
Statyczna biblioteka ICA.

%prep
%setup -q -n libica-%{version}
%patch -P0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	CPPFLAGS="%{rpmcppflags} -I$(pwd)/include"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog LICENSE README.md
%attr(755,root,root) %{_bindir}/icainfo
%attr(755,root,root) %{_bindir}/icainfo-cex
%attr(755,root,root) %{_bindir}/icastats
%attr(755,root,root) %{_libdir}/libica.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libica.so.4
%attr(755,root,root) %{_libdir}/libica-cex.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libica-cex.so.4
%{_mandir}/man1/icainfo.1*
%{_mandir}/man1/icainfo-cex.1*
%{_mandir}/man1/icastats.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libica.so
%attr(755,root,root) %{_libdir}/libica-cex.so
%{_libdir}/libica.la
%{_libdir}/libica-cex.la
%{_includedir}/ica_api.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libica.a
%{_libdir}/libica-cex.a
