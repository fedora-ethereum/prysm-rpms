Summary:	An implementation of BLS threshold signature
Name:		bls
Version:	1.35
Release:	%autorelease
License:	BSD
URL:		https://github.com/herumi/%{name}
Source0:	https://github.com/herumi/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch1:		bls-0001-Use-shared-mcl.patch
Patch2:		bls-0002-Use-LIB_SUFFIX.patch
Patch3:		bls-0003-Use-shared-cmake-dir.patch
BuildRequires:	cmake
BuildRequires:	libtool
BuildRequires:	make
BuildRequires:	mcl-devel
BuildRequires:  gcc-c++


%description
An implementation of BLS threshold signature, which supports the new BLS
Signatures specified at Ethereum 2.0 Phase 0.


%package devel
Summary:	Development files for bls
Requires:	%{name}%{?_isa} = %{version}-%{release}


%description devel
Development files for bls.


%prep
%autosetup -p1

%build
%cmake . -DCMAKE_BUILD_TYPE=Release
%cmake_build


%install
%cmake_install


%check
#make test


%files
%{_libdir}/libbls256.so.1.10
%{_libdir}/libbls384.so.1.10
%{_libdir}/libbls384_256.so.1.10


%files devel
%{_datadir}/cmake/Modules/blsTargets-release.cmake
%{_datadir}/cmake/Modules/blsTargets.cmake
%{_includedir}/%{name}
%{_libdir}/libbls256.so
%{_libdir}/libbls384.so
%{_libdir}/libbls384_256.so


%changelog
%autochangelog
