# Generated by go2rpm 1.8.2
%bcond_without check

# https://github.com/ethereum/go-ethereum
%global goipath         github.com/ethereum/go-ethereum
Version:                1.11.5

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
Official Go implementation of the Ethereum protocol.}

%global golicenses      COPYING COPYING.LESSER crypto/bn256/LICENSE\\\
                        crypto/bn256/cloudflare/LICENSE crypto/ecies/LICENSE\\\
                        crypto/secp256k1/LICENSE\\\
                        crypto/secp256k1/libsecp256k1/COPYING log/LICENSE\\\
                        metrics/LICENSE metrics/influxdb/LICENSE
%global godocs          docs AUTHORS README.md SECURITY.md\\\
                        accounts/scwallet/README.md build/checksums.txt\\\
                        build/ci-notes.md cmd/checkpoint-admin/README.md docs\\\
                        cmd/clef/README.md cmd/clef/datatypes.md\\\
                        cmd/clef/extapi_changelog.md\\\
                        cmd/clef/intapi_changelog.md\\\
                        cmd/clef/requirements.txt cmd/clef/rules.md\\\
                        cmd/clef/tutorial.md cmd/devp2p/README.md\\\
                        cmd/ethkey/README.md cmd/evm/README.md\\\
                        cmd/faucet/README.md crypto/ecies/README\\\
                        crypto/secp256k1/libsecp256k1/README.md\\\
                        crypto/secp256k1/libsecp256k1/TODO log/CONTRIBUTORS\\\
                        log/README.md log/README_ETHEREUM.md metrics/FORK.md\\\
                        metrics/README.md metrics/memory.md\\\
                        metrics/influxdb/README.md examples\\\
                        p2p/simulations/README.md swarm/README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Official Go implementation of the Ethereum protocol

License:        GPL-3.0-only AND BSD-3-Clause AND BSD-2-Clause-Views AND Apache-2.0 AND MIT
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep

%generate_buildrequires
%go_generate_buildrequires

%build
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
for cmd in rlp/rlpgen miner/stress/1559 core build miner/stress/beacon miner/stress/ethash miner/stress/clique; do
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
%license COPYING COPYING.LESSER crypto/bn256/LICENSE
%license crypto/bn256/cloudflare/LICENSE crypto/ecies/LICENSE
%license crypto/secp256k1/LICENSE crypto/secp256k1/libsecp256k1/COPYING
%license log/LICENSE metrics/LICENSE metrics/influxdb/LICENSE
%doc docs AUTHORS README.md SECURITY.md accounts/scwallet/README.md
%doc build/checksums.txt build/ci-notes.md cmd/checkpoint-admin/README.md docs
%doc cmd/clef/README.md cmd/clef/datatypes.md cmd/clef/extapi_changelog.md
%doc cmd/clef/intapi_changelog.md cmd/clef/requirements.txt cmd/clef/rules.md
%doc cmd/clef/tutorial.md cmd/devp2p/README.md cmd/ethkey/README.md
%doc cmd/evm/README.md cmd/faucet/README.md crypto/ecies/README
%doc crypto/secp256k1/libsecp256k1/README.md crypto/secp256k1/libsecp256k1/TODO
%doc log/CONTRIBUTORS log/README.md log/README_ETHEREUM.md metrics/FORK.md
%doc metrics/README.md metrics/memory.md metrics/influxdb/README.md examples
%doc p2p/simulations/README.md swarm/README.md
%{_bindir}/*

%gopkgfiles

%changelog
%autochangelog
