# Generated by go2rpm 1.8.2
%bcond_without check
%global debug_package %{nil}

# https://github.com/umbracle/gohashtree
%global goipath         github.com/umbracle/gohashtree
Version:                0.0.2
%global commit		676202ebf441956f62fd350cbac0cc88d5c5bf8c

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
Fork of prysmaticlabs/gohashtree with the branch for continous slices of input
data.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Fork of prysmaticlabs/gohashtree with the branch for continous slices of input data

License:        MIT
URL:            %{gourl}
Source:         %{gosource}

%if %{with check}
# Tests
BuildRequires:  golang(github.com/minio/sha256-simd)
# FIXME this looks like a mistake
BuildRequires:  golang(github.com/prysmaticlabs/gohashtree)
%endif

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
