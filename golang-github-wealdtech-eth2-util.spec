# Generated by go2rpm 1.8.2
%bcond_without check
%global debug_package %{nil}

# https://github.com/wealdtech/go-eth2-util
%global goipath         github.com/wealdtech/go-eth2-util
Version:                1.8.0

# REMOVE BEFORE SUBMITTING THIS FOR REVIEW
# ---
# New Fedora packages should use %%gometa -f, which makes the package
# ExclusiveArch to %%golang_arches_future and thus excludes the package from
# %%ix86. If the new package is needed as a dependency for another pacage,
# please consider removing that package from %%ix86 in the same way, instead of
# building more go packages for i686. If your package is not a leaf package,
# you'll need to coordinate the removal of the package's dependents first.
# ---
# REMOVE BEFORE SUBMITTING THIS FOR REVIEW
%gometa -f

%global common_description %{expand:
Go library providing utilities for Ethereum 2.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        None

License:        Apache-2.0
URL:            %{gourl}
Source:         %{gosource}
# FIXME should go to herumi/bls-eth-go-binary
BuildRequires:	mcl-devel
# FIXME should go to herumi/bls-eth-go-binary
BuildRequires:	bls-devel
BuildRequires:	gcc-c++

%description %{common_description}

%gopkg

%prep
%goprep

%generate_buildrequires
%go_generate_buildrequires

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
%autochangelog
