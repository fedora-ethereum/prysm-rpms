# Generated by go2rpm 1.8.2
%bcond_without check

# https://github.com/btcsuite/btcd
%global goipath         github.com/btcsuite/btcd
Version:                btcutil/psbt/v1.1.7
%global tag             btcutil/psbt/v1.1.7

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
An alternative full node bitcoin implementation written in Go (golang).}

%global golicenses      LICENSE btcutil/LICENSE txscript/data/LICENSE
%global godocs          docs README.md addrmgr/test_coverage.txt\\\
                        blockchain/README.md\\\
                        blockchain/fullblocktests/README.md\\\
                        blockchain/indexers/README.md btcec/README.md\\\
                        btcjson/CONTRIBUTORS btcjson/README.md\\\
                        btcutil/README.md btcutil/base58/README.md\\\
                        btcutil/bech32/README.md btcutil/bloom/README.md\\\
                        btcutil/bloom/test_coverage.txt\\\
                        btcutil/coinset/README.md\\\
                        btcutil/coinset/test_coverage.txt\\\
                        btcutil/gcs/README.md btcutil/hdkeychain/README.md\\\
                        btcutil/hdkeychain/test_coverage.txt\\\
                        btcutil/txsort/README.md chaincfg/README.md\\\
                        chaincfg/chainhash/README.md connmgr/README.md\\\
                        database/README.md database/ffldb/README.md\\\
                        integration/README.md integration/rpctest/README.md\\\
                        mempool/README.md mining/README.md\\\
                        mining/cpuminer/README.md netsync/README.md\\\
                        peer/README.md release/README.md examples\\\
                        rpcclient/CONTRIBUTORS rpcclient/README.md\\\
                        txscript/README.md wire/README.md

Name:           %{goname}
Release:        %autorelease
Summary:        An alternative full node bitcoin implementation written in Go (golang)

License:        ISC
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
%gobuild -o %{gobuilddir}/bin/btcd %{goipath}
for cmd in btcutil/base58; do
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
%license LICENSE btcutil/LICENSE txscript/data/LICENSE
%doc docs README.md addrmgr/test_coverage.txt blockchain/README.md
%doc blockchain/fullblocktests/README.md blockchain/indexers/README.md
%doc btcec/README.md btcjson/CONTRIBUTORS btcjson/README.md btcutil/README.md
%doc btcutil/base58/README.md btcutil/bech32/README.md btcutil/bloom/README.md
%doc btcutil/bloom/test_coverage.txt btcutil/coinset/README.md
%doc btcutil/coinset/test_coverage.txt btcutil/gcs/README.md
%doc btcutil/hdkeychain/README.md btcutil/hdkeychain/test_coverage.txt
%doc btcutil/txsort/README.md chaincfg/README.md chaincfg/chainhash/README.md
%doc connmgr/README.md database/README.md database/ffldb/README.md
%doc integration/README.md integration/rpctest/README.md mempool/README.md
%doc mining/README.md mining/cpuminer/README.md netsync/README.md peer/README.md
%doc release/README.md examples rpcclient/CONTRIBUTORS rpcclient/README.md
%doc txscript/README.md wire/README.md
%{_bindir}/*

%gopkgfiles

%changelog
%autochangelog
