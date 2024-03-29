# Generated by go2rpm 1.9.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/aristanetworks/glog
%global goipath         github.com/aristanetworks/glog
%global commit          4bbe49d210b0a1dd0b1609a31630a5d04169b2ab

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
Leveled execution logs for Go.}

%global golicenses      LICENSE
%global godocs          README

Name:           %{goname}
Version:        0
Release:        %autorelease -p
Summary:        Leveled execution logs for Go

License:        Apache-2.0
URL:            %{gourl}
Source:         %{gosource}

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
%gocheck
%endif

%gopkgfiles

%changelog
%autochangelog
