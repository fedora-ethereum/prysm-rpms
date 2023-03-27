# Generated by go2rpm 1.8.2
%bcond_without check

# https://github.com/aristanetworks/goarista
%global goipath         github.com/aristanetworks/goarista
Version:                0.0.5
%global tag             ockafka-v0.0.5
%global commit          8770395e9995d6eedd11a47e4980f2907c51de40

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
Fairly general building blocks used in Arista Go code and open-sourced for the
benefit of all.}

%global golicenses      COPYING monitor/stats/LICENSE
%global godocs          AUTHORS README.md cmd/README.md cmd/gnmi/README.md\\\
                        cmd/gnmireverse_client/README.md cmd/occli/README.md\\\
                        cmd/ockafka/README.md cmd/ocprometheus/README.md\\\
                        cmd/ocredis/README.md cmd/ocsplunk/README.md\\\
                        cmd/octsdb/README.md cmd/openconfigbeat/README.md\\\
                        gnmireverse/README.md monitor/stats/README

Name:           %{goname}
Release:        %autorelease
Summary:        Fairly general building blocks used in Arista Go code and open-sourced for the benefit of all

License:        BSD-3-Clause AND Apache-2.0
URL:            %{gourl}
Source:         %{gosource}
Patch1:		golang-github-aristanetworks-goarista-0001-goarista-openconfig-use-GNMI-proto-instead-of-OpenCo.patch
Patch2:		golang-github-aristanetworks-goarista-0002-kafka-Drop-support-for-openconfig.proto.patch

%description %{common_description}

%gopkg

%prep
%goprep
%autopatch -p1

%generate_buildrequires
%go_generate_buildrequires

%build
for cmd in gnmi gnmireverse_client gnmireverse_server importsort json2test ockafka ocprometheus ocredis ocsplunk octsdb test2influxdb ; do
  %gobuild -o %{gobuilddir}/bin/$cmd %{goipath}/cmd/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license COPYING monitor/stats/LICENSE
%doc AUTHORS README.md cmd/README.md cmd/gnmi/README.md
%doc cmd/gnmireverse_client/README.md cmd/occli/README.md cmd/ockafka/README.md
%doc cmd/ocprometheus/README.md cmd/ocredis/README.md cmd/ocsplunk/README.md
%doc cmd/octsdb/README.md cmd/openconfigbeat/README.md gnmireverse/README.md
%doc monitor/stats/README
%{_bindir}/*

%gopkgfiles

%changelog
%autochangelog
