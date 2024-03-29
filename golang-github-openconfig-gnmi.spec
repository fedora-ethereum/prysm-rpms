# Generated by go2rpm 1.9.0
%bcond_without check

# https://github.com/openconfig/gnmi
%global goipath         github.com/openconfig/gnmi
Version:                0.9.1

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
GRPC Network Management Interface.}

%global golicenses      LICENSE
%global godocs          CONTRIBUTING.md README.md\\\
                        cmd/gnmi_collector/docker/README.md\\\
                        testing/fake/gnmi/cmd/fake_server/README.md\\\
                        testing/fake/gnmi/cmd/fake_server/config.pb.txt\\\
                        testing/fake/gnmi/cmd/fake_server/example-\\\
                        config.pb.txt

Name:           %{goname}
Release:        %autorelease
Summary:        GRPC Network Management Interface

License:        Apache-2.0
URL:            %{gourl}
Source:         %{gosource}
#Patch1:		golang-github-openconfig-gnmi-0001-Bootstrap-w-o-ygot-support.patch

%description %{common_description}

%gopkg

%prep
%goprep
%autopatch -p1

%generate_buildrequires
%go_generate_buildrequires

%build
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
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
%license LICENSE
%doc CONTRIBUTING.md README.md cmd/gnmi_collector/docker/README.md
%doc testing/fake/gnmi/cmd/fake_server/README.md
%doc testing/fake/gnmi/cmd/fake_server/config.pb.txt
%doc testing/fake/gnmi/cmd/fake_server/example-config.pb.txt
%{_bindir}/*

%gopkgfiles

%changelog
%autochangelog
