# Generated by go2rpm 1.8.2
%bcond_without check
%global debug_package %{nil}

# https://github.com/census-ecosystem/opencensus-go-exporter-jaeger
%global goipath         contrib.go.opencensus.io/exporter/jaeger
%global forgeurl	https://github.com/census-ecosystem/opencensus-go-exporter-jaeger
Version:                0.2.1

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
# FIXME}

%global golicenses      LICENSE
%global godocs          example README.md

Name:           %{goname}
Release:        %autorelease
Summary:        None

License:        Apache-2.0
URL:            %{gourl}
Source:         %{gosource}
# Taken from https://github.com/census-ecosystem/opencensus-go-exporter-jaeger/pull/22
Patch1:		golang-contrib-opencensus-exporter-jaeger-0001-Update-agent.go-1.patch

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
