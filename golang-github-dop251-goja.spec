# Generated by go2rpm 1.9.0
%bcond_without check

# https://github.com/dop251/goja
%global goipath         github.com/dop251/goja
%global commit          e2f543bf4b4c03d1f86e5acde716acdfab08304b

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
ECMAScript/JavaScript engine in pure Go.}

%global golicenses      LICENSE ftoa/LICENSE_LUCENE
%global godocs          README.md ast/README.markdown file/README.markdown\\\
                        parser/README.markdown token/README.markdown

Name:           %{goname}
Version:        0
Release:        %autorelease -p
Summary:        ECMAScript/JavaScript engine in pure Go

License:        MIT
URL:            %{gourl}
Source:         %{gosource}
#Patch1:		golang-github-dop251-goja-0001-Bootstrap-w-o-nodejs-support.patch
BuildRequires:	golang(github.com/dop251/goja_nodejs/console)
BuildRequires:	golang(github.com/dop251/goja_nodejs/require)

%description %{common_description}

%gopkg

%prep
%goprep
%autopatch -p1

%generate_buildrequires
%go_generate_buildrequires

%build
for cmd in goja; do
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
%license LICENSE ftoa/LICENSE_LUCENE
%doc README.md ast/README.markdown file/README.markdown parser/README.markdown
%doc token/README.markdown
%{_bindir}/*

%gopkgfiles

%changelog
%autochangelog
