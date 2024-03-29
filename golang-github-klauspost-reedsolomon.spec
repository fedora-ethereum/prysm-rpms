# Generated by go2rpm 1.9.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/klauspost/reedsolomon
%global goipath         github.com/klauspost/reedsolomon
Version:                1.11.7

# REMOVE BEFORE SUBMITTING THIS FOR REVIEW
# ---
# New Fedora packages should use %%gometa -f, which makes the package
# ExclusiveArch to %%golang_arches_future and thus excludes the package from
# %%ix86. If the new package is needed as a dependency for another package,
# please consider removing that package from %%ix86 in the same way, instead of
# building more go packages for i686. If your package is not a leaf package,
# you'll need to coordinate the removal of the package's dependents first.
# ---
# REMOVE BEFORE SUBMITTING THIS FOR REVIEW
%gometa -f


%global common_description %{expand:
Reed-Solomon Erasure Coding in Go.}

%global golicenses      LICENSE
%global godocs          examples README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Reed-Solomon Erasure Coding in Go

License:        MIT
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep
%autopatch -p1

%generate_buildrequires
%go_generate_buildrequires

%build
%gobuild -o %{gobuilddir}/bin/reedsolomon %{goipath}

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc examples README.md

%gopkgfiles

%changelog
%autochangelog
