# Disable the debug package as we don't provide it:
%global debug_package %{nil}
# TODO: rig up debug package support with golang.

%global git_commit aa7d0df7ff5f74168bdaf93453c856f279ec1573

Name:           prysm
Version:        4.0.5
Release:        %autorelease
Summary:        An Ethereum Consensus Implementation
License:        MIT AND Apache-2.0 AND MPL-2.0 AND GPL-3.0-only
URL:            https://github.com/prysmaticlabs/%{name}
Source0:        https://github.com/prysmaticlabs/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires: gcc >= 10
BuildRequires: gcc-c++ >= 10
BuildRequires: git
BuildRequires: golang
BuildRequires: systemd-rpm-macros

%description
A Golang implementation of the Ethereum Consensus specification.


%prep
# Build fails with GCC Go, so die unless we can set that alternative:
%autosetup -p1

%build
export GOPATH="${PWD}/go"
export PATH="${GOPATH}/bin:${PATH}"
export GIT_COMMIT="%{git_commit}"
export GIT_BRANCH="%{name}-v%{version}"
export GIT_TAG="v%{version}"
# Begin building:
echo "------------ Building Prysm $GIT_TAG from branch $GIT_BRANCH (commit $GIT_COMMIT) ------------"
make %{name} downloader hack integration observer rpcdaemon rpctest sentry state txpool
echo '# "%{name}" 1 "%{summary}" %{vendor} "User Manuals"' > %{name}.1.md
# Rename binaries with common names to [name]-[binary] scheme:
cd build/bin
for binary in *; do
    %{__strip} --strip-debug --strip-unneeded ${binary}
    if echo ${binary} | grep -qv '^%{name}'; then
        %{__mv} ${binary} %{name}-${binary}
    fi
done
# Trash the temporary Go build chain:
chmod -R ug+w ${GOPATH}
rm -rf ${GOPATH}


%install
%{__install} -m 0755 -D ./build/bin/* -t %{buildroot}%{_bindir}


%files
%license LICENSE.md
%doc CONTRIBUTING.md INTEROP.md README.md SECURITY.md TERMS_OF_SERVICE.md
%{_bindir}/*


%pre
if ! getent group %{name} &> /dev/null; then
    groupadd -r %{name}
fi
if ! getent passwd %{name} &> /dev/null; then
    useradd -r -g %{name} -m -d %{_sharedstatedir}/%{name} -k /dev/null %{name}
fi


%changelog
%autochangelog
