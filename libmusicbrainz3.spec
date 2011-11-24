%define package_name    libmusicbrainz
%define	version	3.0.3
%define release	%mkrel 2

%define api 3
%define major 6
%define libname %mklibname musicbrainz %api %{major}
%define develname %mklibname -d musicbrainz %api

Name:		libmusicbrainz3
Version:	%{version}
Release:	%{release}
Summary:	A software library for accesing MusicBrainz servers
Source:		http://ftp.musicbrainz.org/pub/musicbrainz/%{package_name}-%{version}.tar.gz
URL:		http://musicbrainz.org/doc/libmusicbrainz
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
License:	LGPLv2+
BuildRequires:  cmake
BuildRequires:  libneon-devel
BuildRequires:  libdiscid-devel
BuildRequires:  libcppunit-devel

%description
The MusicBrainz client library allows applications to make metadata
lookup to a MusicBrainz server, generate signatures from WAV data and
create CD Index Disk ids from audio CD roms.

%package -n %{libname}
Summary:	A software library for accesing MusicBrainz servers
Group:		System/Libraries

%description -n %{libname}
The MusicBrainz client library allows applications to make metadata
lookup to a MusicBrainz server, generate signatures from WAV data and
create CD Index Disk ids from audio CD roms.

%package -n %develname
Summary:	Headers for developing programs that will use libmusicbrainz
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%develname
This package contains the headers that programmers will need to develop
applications which will use libmusicbrainz.



%prep
%setup -q -n %{package_name}-%{version}

%build
cmake . -DCMAKE_INSTALL_PREFIX=%_prefix \
%if "%_lib" != "lib"
    -DLIB_SUFFIX=64 \
%endif


%make


%install
rm -rf %{buildroot}

%makeinstall_std


%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif


%files -n %{libname}
%defattr(-, root, root)
%doc AUTHORS.txt COPYING.txt NEWS.txt README.txt
%{_libdir}/libmusicbrainz%{api}.so.%{major}*

%files -n %develname
%defattr(-, root, root)
%{_includedir}/musicbrainz%{api}
%{_libdir}/*.so
%{_libdir}/pkgconfig/libmusicbrainz%{api}.pc
