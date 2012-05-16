%define package_name    libmusicbrainz
%define	version	4.0.2
%define release	1

%define api 4
%define major 3
%define libname %mklibname musicbrainz %api %{major}
%define develname %mklibname -d musicbrainz %api

Name:		libmusicbrainz4
Version:	%{version}
Release:	%{release}
Summary:	A software library for accesing MusicBrainz servers
Source0:	https://github.com/downloads/metabrainz/libmusicbrainz/%{package_name}-%{version}.tar.gz
Patch0:		cmake_include_dir.patch
Patch1:		libmusicbrainz-4.0.2-remove-unused-variable.patch
URL:		http://musicbrainz.org/doc/libmusicbrainz
Group:		Sound
License:	LGPLv2+
BuildRequires:  cmake
BuildRequires:	pkgconfig(neon)
BuildRequires:	pkgconfig(libdiscid)
BuildRequires:	pkgconfig(cppunit)

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
%apply_patches

%build
cmake . -DCMAKE_INSTALL_PREFIX=%_prefix \
%if "%_lib" != "lib"
    -DLIB_SUFFIX=64 \
%endif

%make

%install

%makeinstall_std

%files -n %{libname}
%doc AUTHORS.txt COPYING.txt NEWS.txt
%{_libdir}/libmusicbrainz%{api}.so.%{major}*

%files -n %develname
%{_includedir}/musicbrainz%{api}
%{_libdir}/*.so
%{_libdir}/pkgconfig/libmusicbrainz%{api}.pc
