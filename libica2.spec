Summary:	Interface library to the ICA device driver
Summary(pl.UTF-8):	Biblioteka interfejsu do sterownika urządzenia ICA
Name:		libica2
Version:	3.0.2
Release:	1
License:	CPL v1.0
Group:		Libraries
Source0:	http://downloads.sourceforge.net/opencryptoki/libica-%{version}.tgz
# Source0-md5:	0fa3a49050db6b987b7ff8d62bff3709
Patch0:		%{name}-headers.patch
URL:		http://opencryptoki.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.9.5
BuildRequires:	libtool
BuildRequires:	openssl-devel
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
Requires:	openssl-devel
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
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
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
%doc AUTHORS ChangeLog LICENSE
%attr(755,root,root) %{_bindir}/icainfo
%attr(755,root,root) %{_bindir}/icastats
%attr(755,root,root) %{_libdir}/libica.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libica.so.3
%{_mandir}/man1/icainfo.1*
%{_mandir}/man1/icastats.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libica.so
%{_libdir}/libica.la
%{_includedir}/ica_api.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libica.a
