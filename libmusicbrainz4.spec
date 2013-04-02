%define package_name    libmusicbrainz
%define	version	4.0.2
%define release	1
%define debug_package          %{nil}

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
Patch1:		libmusicbrainz-4.0.2-remove-wextra-warnings.patch
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


%changelog
* Wed May 16 2012 Götz Waschk <waschk@mandriva.org> 4.0.2-1
+ Revision: 799136
- fix a build error
- new version
- fix source URL

* Thu Apr 26 2012 Alexander Khrukin <akhrukin@mandriva.org> 4.0.1-1
+ Revision: 793553
- version update 4.0.1

* Tue Feb 21 2012 Götz Waschk <waschk@mandriva.org> 4.0.0-1
+ Revision: 778601
- new major
- update build deps
- new version
- fix build

  + Alexander Khrukin <akhrukin@mandriva.org>
    - pkgconfig(libname) instead of libname-devel

* Thu Nov 24 2011 Götz Waschk <waschk@mandriva.org> 4.0.0-0.beta2.1
+ Revision: 733141
- new version with a new API

* Fri Apr 29 2011 Oden Eriksson <oeriksson@mandriva.com> 3.0.3-2
+ Revision: 660268
- mass rebuild

* Wed Oct 20 2010 Götz Waschk <waschk@mandriva.org> 3.0.3-1mdv2011.0
+ Revision: 586907
- new version
- drop patch

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 3.0.2-3mdv2010.1
+ Revision: 520889
- rebuilt for 2010.1

* Wed May 20 2009 Götz Waschk <waschk@mandriva.org> 3.0.2-2mdv2010.0
+ Revision: 377955
- fix for gcc 4.4

* Thu Oct 16 2008 Götz Waschk <waschk@mandriva.org> 3.0.2-1mdv2009.1
+ Revision: 294297
- new version
- drop patch

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 3.0.1-4mdv2009.0
+ Revision: 267922
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun May 25 2008 Götz Waschk <waschk@mandriva.org> 3.0.1-3mdv2009.0
+ Revision: 211251
- fix build with gcc 4.3

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Oct 23 2007 Götz Waschk <waschk@mandriva.org> 3.0.1-2mdv2008.1
+ Revision: 101485
- fix cmake call to have the right libdir on x86_64
- import libmusicbrainz3

