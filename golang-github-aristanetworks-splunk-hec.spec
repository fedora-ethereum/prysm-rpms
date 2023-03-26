# Generated by go2rpm 1.9.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/aristanetworks/splunk-hec-go
%global goipath         github.com/aristanetworks/splunk-hec-go
Version:                0.3.3

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
Splunk HTTP Event Collector (HEC) Golang library.}

%global golicenses      LICENSE
%global godocs          example README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Splunk HTTP Event Collector (HEC) Golang library

License:        Apache-2.0
URL:            %{gourl}
Source:         %{gosource}
Patch1:		golang-github-aristanetworks-splunk-hec-0001-Use-main-package.patch
Patch2:		golang-github-aristanetworks-splunk-hec-0002-Use-a-new-API.patch

%description %{common_description}

%gopkg

%prep
%goprep
%autopatch -p1

%generate_buildrequires
%go_generate_buildrequires

%install
%gopkginstall

%if %{with check}
%check
# FIXME requires test server up and running
#%%gocheck
%endif

%gopkgfiles

%changelog
%autochangelog
