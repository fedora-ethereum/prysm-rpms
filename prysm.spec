# Generated by go2rpm 1.8.2
%bcond_without check

# https://github.com/prysmaticlabs/prysm
%global goipath         github.com/prysmaticlabs/prysm
Version:                3.2.0

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
Go implementation of Ethereum proof of stake.}

%global golicenses      LICENSE.md container/leaky-bucket/LICENSE\\\
                        container/queue/LICENSE proto/eth/LICENSE\\\
                        runtime/logging/logrus-prefixed-formatter/LICENSE\\\
                        third_party/usb/LICENSE
%global godocs          CONTRIBUTING.md INTEROP.md README.md SECURITY.md\\\
                        TERMS_OF_SERVICE.md DEPENDENCIES.md .well-\\\
                        known/security.txt beacon-chain/README.md\\\
                        config/features/README.md contracts/deposit/README.md\\\
                        hack/README.md hack/beacon-node-api/README.md\\\
                        hack/keymanager-api/README.md\\\
                        monitoring/clientstats/README.md\\\
                        monitoring/prometheus/README.md\\\
                        monitoring/tracing/README.md proto/README.md\\\
                        proto/eth/v1/README.md proto/prysm/v1alpha1/README.md\\\
                        proto/prysm/v1alpha1/swagger_description.md\\\
                        runtime/logging/logrus-prefixed-formatter/README.md\\\
                        testing/benchmark/README.md\\\
                        testing/endtoend/README.md testing/spectest/README.md\\\
                        third_party/README.md third_party/usb/AUTHORS\\\
                        third_party/usb/README.md tools/analyzers/README.md\\\
                        tools/analyzers/gocognit/README.md tools/cross-\\\
                        toolchain/README.md tools/enr-calculator/README.md\\\
                        tools/eth1voting/README.md tools/pcli/README.md\\\
                        tools/specs-checker/README.md tools/specs-\\\
                        checker/data/extra.md tools/specs-\\\
                        checker/data/specs/phase0/beacon-chain.md\\\
                        tools/specs-checker/data/specs/phase0/fork-choice.md\\\
                        tools/specs-checker/data/specs/phase0/validator.md\\\
                        tools/specs-checker/data/specs/phase0/weak-\\\
                        subjectivity.md tools/specs-checker/data/ssz/merkle-\\\
                        proofs.md tools/unencrypted-keys-gen/README.md\\\
                        validator/README.md validator/keymanager/remote-\\\
                        web3signer/README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Go implementation of Ethereum proof of stake

License:        MIT AND Apache-2.0 AND MPL-2.0 AND GPL-3.0-only
URL:            %{gourl}
Source:         %{gosource}
Patch1:		prysm-0001-Consistently-import-messagediff.patch

BuildRequires: golang(contrib.go.opencensus.io/exporter/jaeger)
BuildRequires: golang(github.com/MariusVanDerWijden/FuzzyVM/filler)
BuildRequires: golang(github.com/MariusVanDerWijden/tx-fuzz)
BuildRequires: golang(github.com/aristanetworks/goarista/monotime)
BuildRequires: golang(github.com/bazelbuild/rules_go/go/tools/bazel)
BuildRequires: golang(github.com/btcsuite/btcd/btcec/v2)
BuildRequires: golang(github.com/d4l3k/messagediff)
BuildRequires: golang(github.com/d4l3k/messagediff)
BuildRequires: golang(github.com/dgraph-io/ristretto)
BuildRequires: golang(github.com/dustin/go-humanize)
BuildRequires: golang(github.com/emicklei/dot)
BuildRequires: golang(github.com/ethereum/go-ethereum)
BuildRequires: golang(github.com/ethereum/go-ethereum/accounts)
BuildRequires: golang(github.com/ethereum/go-ethereum/accounts/abi)
BuildRequires: golang(github.com/ethereum/go-ethereum/accounts/abi/bind)
BuildRequires: golang(github.com/ethereum/go-ethereum/accounts/abi/bind/backends)
BuildRequires: golang(github.com/ethereum/go-ethereum/accounts/keystore)
BuildRequires: golang(github.com/ethereum/go-ethereum/cmd/utils)
BuildRequires: golang(github.com/ethereum/go-ethereum/common)
BuildRequires: golang(github.com/ethereum/go-ethereum/common/fdlimit)
BuildRequires: golang(github.com/ethereum/go-ethereum/common/hexutil)
BuildRequires: golang(github.com/ethereum/go-ethereum/console)
BuildRequires: golang(github.com/ethereum/go-ethereum/core)
BuildRequires: golang(github.com/ethereum/go-ethereum/core/types)
BuildRequires: golang(github.com/ethereum/go-ethereum/crypto)
BuildRequires: golang(github.com/ethereum/go-ethereum/eth)
BuildRequires: golang(github.com/ethereum/go-ethereum/eth/downloader)
BuildRequires: golang(github.com/ethereum/go-ethereum/ethclient)
BuildRequires: golang(github.com/ethereum/go-ethereum/event)
BuildRequires: golang(github.com/ethereum/go-ethereum/les)
BuildRequires: golang(github.com/ethereum/go-ethereum/log)
BuildRequires: golang(github.com/ethereum/go-ethereum/metrics)
BuildRequires: golang(github.com/ethereum/go-ethereum/node)
BuildRequires: golang(github.com/ethereum/go-ethereum/p2p/discover)
BuildRequires: golang(github.com/ethereum/go-ethereum/p2p/enode)
BuildRequires: golang(github.com/ethereum/go-ethereum/p2p/enr)
BuildRequires: golang(github.com/ethereum/go-ethereum/params)
BuildRequires: golang(github.com/ethereum/go-ethereum/rpc)
BuildRequires: golang(github.com/fjl/memsize/memsizeui)
BuildRequires: golang(github.com/fsnotify/fsnotify)
BuildRequires: golang(github.com/ghodss/yaml)
BuildRequires: golang(github.com/go-playground/validator/v10)
BuildRequires: golang(github.com/go-yaml/yaml)
BuildRequires: golang(github.com/gogo/protobuf/proto)
BuildRequires: golang(github.com/gogo/protobuf/types)
BuildRequires: golang(github.com/golang-jwt/jwt/v4)
BuildRequires: golang(github.com/golang/gddo/httputil)
BuildRequires: golang(github.com/golang/mock/gomock)
BuildRequires: golang(github.com/golang/protobuf/proto)
BuildRequires: golang(github.com/golang/protobuf/protoc-gen-go/descriptor)
BuildRequires: golang(github.com/golang/protobuf/ptypes/empty)
BuildRequires: golang(github.com/golang/protobuf/ptypes/timestamp)
BuildRequires: golang(github.com/golang/snappy)
BuildRequires: golang(github.com/google/gofuzz)
BuildRequires: golang(github.com/google/uuid)
BuildRequires: golang(github.com/gorilla/mux)
BuildRequires: golang(github.com/gostaticanalysis/comment)
BuildRequires: golang(github.com/grpc-ecosystem/go-grpc-middleware)
BuildRequires: golang(github.com/grpc-ecosystem/go-grpc-middleware/recovery)
BuildRequires: golang(github.com/grpc-ecosystem/go-grpc-middleware/retry)
BuildRequires: golang(github.com/grpc-ecosystem/go-grpc-middleware/tracing/opentracing)
BuildRequires: golang(github.com/grpc-ecosystem/go-grpc-prometheus)
BuildRequires: golang(github.com/grpc-ecosystem/grpc-gateway/v2/proto/gateway)
BuildRequires: golang(github.com/grpc-ecosystem/grpc-gateway/v2/runtime)
BuildRequires: golang(github.com/grpc-ecosystem/grpc-gateway/v2/utilities)
BuildRequires: golang(github.com/hashicorp/golang-lru)
BuildRequires: golang(github.com/herumi/bls-eth-go-binary/bls)
BuildRequires: golang(github.com/holiman/uint256)
BuildRequires: golang(github.com/ipfs/go-log/v2)
BuildRequires: golang(github.com/joonix/log)
BuildRequires: golang(github.com/json-iterator/go)
BuildRequires: golang(github.com/k0kubun/go-ansi)
BuildRequires: golang(github.com/kr/pretty)
BuildRequires: golang(github.com/libp2p/go-libp2p)
BuildRequires: golang(github.com/libp2p/go-libp2p-pubsub)
BuildRequires: golang(github.com/libp2p/go-libp2p-pubsub/pb)
BuildRequires: golang(github.com/libp2p/go-libp2p/config)
BuildRequires: golang(github.com/libp2p/go-libp2p/core)
BuildRequires: golang(github.com/libp2p/go-libp2p/core/connmgr)
BuildRequires: golang(github.com/libp2p/go-libp2p/core/control)
BuildRequires: golang(github.com/libp2p/go-libp2p/core/crypto)
BuildRequires: golang(github.com/libp2p/go-libp2p/core/event)
BuildRequires: golang(github.com/libp2p/go-libp2p/core/host)
BuildRequires: golang(github.com/libp2p/go-libp2p/core/network)
BuildRequires: golang(github.com/libp2p/go-libp2p/core/peer)
BuildRequires: golang(github.com/libp2p/go-libp2p/core/peerstore)
BuildRequires: golang(github.com/libp2p/go-libp2p/core/protocol)
BuildRequires: golang(github.com/libp2p/go-libp2p/p2p/host/blank)
BuildRequires: golang(github.com/libp2p/go-libp2p/p2p/host/peerstore/test)
BuildRequires: golang(github.com/libp2p/go-libp2p/p2p/muxer/mplex)
BuildRequires: golang(github.com/libp2p/go-libp2p/p2p/net/swarm/testing)
BuildRequires: golang(github.com/libp2p/go-libp2p/p2p/protocol/identify)
BuildRequires: golang(github.com/libp2p/go-libp2p/p2p/security/noise)
BuildRequires: golang(github.com/libp2p/go-libp2p/p2p/transport/tcp)
BuildRequires: golang(github.com/logrusorgru/aurora)
BuildRequires: golang(github.com/manifoldco/promptui)
BuildRequires: golang(github.com/mgutz/ansi)
BuildRequires: golang(github.com/minio/highwayhash)
BuildRequires: golang(github.com/minio/sha256-simd)
BuildRequires: golang(github.com/mohae/deepcopy)
BuildRequires: golang(github.com/multiformats/go-multiaddr)
BuildRequires: golang(github.com/multiformats/go-multiaddr/net)
BuildRequires: golang(github.com/patrickmn/go-cache)
BuildRequires: golang(github.com/paulbellamy/ratecounter)
BuildRequires: golang(github.com/pborman/uuid)
BuildRequires: golang(github.com/pkg/errors)
BuildRequires: golang(github.com/prometheus/client_golang/prometheus)
BuildRequires: golang(github.com/prometheus/client_golang/prometheus/promauto)
BuildRequires: golang(github.com/prometheus/client_golang/prometheus/promhttp)
BuildRequires: golang(github.com/prometheus/client_model/go)
BuildRequires: golang(github.com/prometheus/prom2json)
BuildRequires: golang(github.com/prysmaticlabs/fastssz)
BuildRequires: golang(github.com/prysmaticlabs/go-bitfield)
BuildRequires: golang(github.com/prysmaticlabs/gohashtree)
BuildRequires: golang(github.com/prysmaticlabs/prombbolt)
BuildRequires: golang(github.com/r3labs/sse)
BuildRequires: golang(github.com/rs/cors)
BuildRequires: golang(github.com/schollz/progressbar/v3)
BuildRequires: golang(github.com/sirupsen/logrus)
BuildRequires: golang(github.com/sirupsen/logrus/hooks/test)
BuildRequires: golang(github.com/status-im/keycard-go/hexutils)
BuildRequires: golang(github.com/stretchr/testify/assert)
BuildRequires: golang(github.com/supranational/blst/bindings/go)
BuildRequires: golang(github.com/thomaso-mirodin/intmath/u64)
BuildRequires: golang(github.com/trailofbits/go-mutexasserts)
BuildRequires: golang(github.com/tyler-smith/go-bip39)
BuildRequires: golang(github.com/tyler-smith/go-bip39/wordlists)
BuildRequires: golang(github.com/urfave/cli/v2)
BuildRequires: golang(github.com/urfave/cli/v2/altsrc)
BuildRequires: golang(github.com/uudashr/gocognit)
BuildRequires: golang(github.com/wealdtech/go-bytesutil)
BuildRequires: golang(github.com/wealdtech/go-eth2-util)
BuildRequires: golang(github.com/wealdtech/go-eth2-wallet-encryptor-keystorev4)
BuildRequires: golang(github.com/wercker/journalhook)
BuildRequires: golang(go.etcd.io/bbolt)
BuildRequires: golang(go.opencensus.io/plugin/ocgrpc)
BuildRequires: golang(go.opencensus.io/trace)
BuildRequires: golang(go.uber.org/automaxprocs/maxprocs)
BuildRequires: golang(golang.org/x/crypto/pbkdf2)
BuildRequires: golang(golang.org/x/crypto/scrypt)
BuildRequires: golang(golang.org/x/crypto/sha3)
BuildRequires: golang(golang.org/x/crypto/ssh/terminal)
BuildRequires: golang(golang.org/x/exp/rand)
BuildRequires: golang(golang.org/x/mod/semver)
BuildRequires: golang(golang.org/x/sync/errgroup)
BuildRequires: golang(golang.org/x/tools/cover)
BuildRequires: golang(golang.org/x/tools/go/analysis)
BuildRequires: golang(golang.org/x/tools/go/analysis/analysistest)
BuildRequires: golang(golang.org/x/tools/go/analysis/passes/inspect)
BuildRequires: golang(golang.org/x/tools/go/ast/astutil)
BuildRequires: golang(golang.org/x/tools/go/ast/inspector)
BuildRequires: golang(golang.org/x/tools/go/types/typeutil)
BuildRequires: golang(google.golang.org/genproto/googleapis/api/annotations)
BuildRequires: golang(google.golang.org/grpc)
BuildRequires: golang(google.golang.org/grpc/codes)
BuildRequires: golang(google.golang.org/grpc/connectivity)
BuildRequires: golang(google.golang.org/grpc/credentials)
BuildRequires: golang(google.golang.org/grpc/grpclog)
BuildRequires: golang(google.golang.org/grpc/metadata)
BuildRequires: golang(google.golang.org/grpc/peer)
BuildRequires: golang(google.golang.org/grpc/reflection)
BuildRequires: golang(google.golang.org/grpc/resolver)
BuildRequires: golang(google.golang.org/grpc/status)
BuildRequires: golang(google.golang.org/protobuf/encoding/protojson)
BuildRequires: golang(google.golang.org/protobuf/proto)
BuildRequires: golang(google.golang.org/protobuf/reflect/protoreflect)
BuildRequires: golang(google.golang.org/protobuf/runtime/protoimpl)
BuildRequires: golang(google.golang.org/protobuf/types/descriptorpb)
BuildRequires: golang(google.golang.org/protobuf/types/known/anypb)
BuildRequires: golang(google.golang.org/protobuf/types/known/emptypb)
BuildRequires: golang(google.golang.org/protobuf/types/known/timestamppb)
BuildRequires: golang(gopkg.in/yaml.v2)
BuildRequires: golang(k8s.io/client-go/tools/cache)

#golang(github.com/wercker/journalhook)


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
for cmd in tools/interop/split-keys tools/interop/export-genesis tools/replay-http tools/beacon-fuzz tools/pcli tools/bootnode tools/keystores tools/eth1voting tools/benchmark-files-gen tools/extractor tools/blocktree tools/gocovmerge beacon-chain/server tools/interop/convert-keys tools/unencrypted-keys-gen tools/eth1exporter tools/enr-calculator tools/http-request-sink tools/specs-checker tools/exploredb tools/forkchecker; do
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
%license LICENSE.md container/leaky-bucket/LICENSE container/queue/LICENSE
%license proto/eth/LICENSE runtime/logging/logrus-prefixed-formatter/LICENSE
%license third_party/usb/LICENSE
%doc CONTRIBUTING.md INTEROP.md README.md SECURITY.md TERMS_OF_SERVICE.md
%doc DEPENDENCIES.md .well-known/security.txt beacon-chain/README.md
%doc config/features/README.md contracts/deposit/README.md hack/README.md
%doc hack/beacon-node-api/README.md hack/keymanager-api/README.md
%doc monitoring/clientstats/README.md monitoring/prometheus/README.md
%doc monitoring/tracing/README.md proto/README.md proto/eth/v1/README.md
%doc proto/prysm/v1alpha1/README.md proto/prysm/v1alpha1/swagger_description.md
%doc runtime/logging/logrus-prefixed-formatter/README.md
%doc testing/benchmark/README.md testing/endtoend/README.md
%doc testing/spectest/README.md third_party/README.md third_party/usb/AUTHORS
%doc third_party/usb/README.md tools/analyzers/README.md
%doc tools/analyzers/gocognit/README.md tools/cross-toolchain/README.md
%doc tools/enr-calculator/README.md tools/eth1voting/README.md
%doc tools/pcli/README.md tools/specs-checker/README.md
%doc tools/specs-checker/data/extra.md
%doc tools/specs-checker/data/specs/phase0/beacon-chain.md
%doc tools/specs-checker/data/specs/phase0/fork-choice.md
%doc tools/specs-checker/data/specs/phase0/validator.md
%doc tools/specs-checker/data/specs/phase0/weak-subjectivity.md
%doc tools/specs-checker/data/ssz/merkle-proofs.md
%doc tools/unencrypted-keys-gen/README.md validator/README.md
%doc validator/keymanager/remote-web3signer/README.md
%{_bindir}/*

%gopkgfiles

%changelog
%autochangelog
