# Generated by go2rpm 1.9.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/garyburd/redigo
%global goipath         github.com/garyburd/redigo
Version:                1.6.4

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
Go client for Redis.}

%global golicenses      LICENSE
%global godocs          README.markdown

Name:           %{goname}
Release:        %autorelease
Summary:        Go client for Redis

License:        Apache-2.0
URL:            %{gourl}
Source:         %{gosource}
# For testing only
BuildRequires:	redis

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
# FIXME tests requires Redis set up and running on port tcp:6379
#%%gocheck
%endif

%gopkgfiles

%changelog
%autochangelog
