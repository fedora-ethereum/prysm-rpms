# Generated by go2rpm 1.9.0
%bcond_without check
%global debug_package %{nil}

# https://gopkg.in/redis.v4
%global goipath         gopkg.in/redis.v4
%global forgeurl        https://github.com/redis/go-redis
Version:                4.2.4

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

%global goaltipaths     github.com/redis/go-redis


%global common_description %{expand:
Type-safe Redis client for Golang.}

%global golicenses      LICENSE
%global godocs          example CHANGELOG.md README.md RELEASING.md\\\
                        extra/redisotel/README.md\\\
                        extra/redisprometheus/README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Type-safe Redis client for Golang

License:        BSD-2-Clause
URL:            %{gourl}
Source:         %{gosource}
BuildRequires:	golang(github.com/garyburd/redigo/redis)

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
