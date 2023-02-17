# Generated by go2rpm 1.8.2
%bcond_without check
%global debug_package %{nil}

# https://github.com/trailofbits/go-mutexasserts
%global goipath         github.com/trailofbits/go-mutexasserts
%global commit          19999e7d3cef20712839127cac0163d1e06743ca

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
A small library that allows to check if Go mutexes are locked.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        %autorelease -p
Summary:        A small library that allows to check if Go mutexes are locked

License:        MIT
URL:            %{gourl}
Source:         %{gosource}

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
# FIXME
# github.com/trailofbits/go-mutexasserts [github.com/trailofbits/go-mutexasserts.test]
# ./asserts_test.go:9:2: undefined: exit
#%%gocheck
%endif

%gopkgfiles

%changelog
%autochangelog
