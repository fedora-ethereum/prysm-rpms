# Generated by go2rpm 1.9.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/tjfoc/gmsm
%global goipath         github.com/tjfoc/gmsm
Version:                1.4.1
%global commit          36b992c51540c71b274f8fdfe0887c8ffa022c89

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
GM SM2/3/4 library based on Golang (基于Go语言的国密SM2/SM3/SM4算法库).}

%global golicenses      LICENSE
%global godocs          API使用说明.md CHANGELOG.md README.md\\\
                        sm4/padding/README.md gmtls/websvr/README.md

Name:           %{goname}
Release:        %autorelease
Summary:        GM SM2/3/4 library based on Golang (基于Go语言的国密SM2/SM3/SM4算法库)

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
