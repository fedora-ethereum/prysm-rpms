Summary:	A portable and fast pairing-based cryptography library
Name:		mcl
Version:	1.80
Release:	%autorelease
License:	BSD
URL:		https://github.com/herumi/%{name}
Source0:	https://github.com/herumi/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch1:		mcl-0001-Add-LIB-prefix.patch
BuildRequires:	gmp-devel
BuildRequires:	libtool
BuildRequires:	make
BuildRequires:  gcc-c++


%description
A portable and fast pairing-based cryptography library.


%package devel
Summary:	Development files for libmcl
# FIXME a proper soname versioning would be nice
#Requires:	%{name}%{?_isa} = %{version}-%{release}


%description devel
A portable and fast pairing-based cryptography library.


%prep
%autosetup -p1

%build
%make_build


%install
PREFIX=%{buildroot}/usr/ LIB=%{_lib} %make_install


%check
#make test


#%%files
# FIXME a proper soname versioning would be nice
# empty


%files devel
%license COPYRIGHT
%{_includedir}/cybozu/
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/lib%{name}.a


%changelog
%autochangelog
