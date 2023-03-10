Summary:	A portable and fast pairing-based cryptography library
Name:		mcl
Version:	1.80
Release:	%autorelease
License:	BSD
URL:		https://github.com/herumi/%{name}
Source0:	https://github.com/herumi/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch1:		mcl-0001-Add-LIB-prefix.patch
Patch2:		mcl-0002-Use-lib-suffix.patch
Patch3:		mcl-0003-Use-shared-cmake-dir.patch
Patch4:		mcl-0004-Change-CMake-file-name.patch
Patch5:		mcl-0005-Don-t-use-CMAKE_INSTALL_DIR.patch
BuildRequires:	gmp-devel
BuildRequires:	libtool
BuildRequires:	make
BuildRequires:	cmake
BuildRequires:  gcc-c++


%description
A portable and fast pairing-based cryptography library.


%package devel
Summary:	Development files for mcl
Requires:	%{name}%{?_isa} = %{version}-%{release}


%description devel
A portable and fast pairing-based cryptography library.


%prep
%autosetup -p1

%build
%cmake . -DMCL_STATIC_LIB=OFF -DMCL_USE_LLVM=OFF -DCMAKE_BUILD_TYPE=Release
%cmake_build


%install
%cmake_install


%check
#make test


%files
%license COPYRIGHT
%{_libdir}/libmcl.so.1
%{_libdir}/libmcl.so.1.74
%{_libdir}/libmclbn256.so.1
%{_libdir}/libmclbn256.so.1.74
%{_libdir}/libmclbn384.so.1
%{_libdir}/libmclbn384.so.1.74
%{_libdir}/libmclbn384_256.so.1
%{_libdir}/libmclbn384_256.so.1.74


%files devel
#%%{_datadir}/cmake/Modules/mclTargets-config.cmake
#%%{_datadir}/cmake/Modules/mclTargets.cmake
%{_datadir}/cmake/Modules/Mcl-release.cmake
%{_datadir}/cmake/Modules/Mcl.cmake
%{_includedir}/%{name}
%{_includedir}/cybozu/
%{_libdir}/lib%{name}.a
%{_libdir}/lib%{name}.so
%{_libdir}/libmclbn256.so
%{_libdir}/libmclbn384.so
%{_libdir}/libmclbn384_256.so


%changelog
%autochangelog
