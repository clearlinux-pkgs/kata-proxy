#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : kata-proxy
Version  : 1.5.0
Release  : 12
URL      : https://github.com/kata-containers/proxy/archive/1.5.0.tar.gz
Source0  : https://github.com/kata-containers/proxy/archive/1.5.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause ISC MIT MPL-2.0-no-copyleft-exception
Requires: kata-proxy-libexec = %{version}-%{release}
Requires: kata-proxy-license = %{version}-%{release}
BuildRequires : buildreq-golang
Patch1: 0001-add-fake-autogen.patch

%description
[![Build Status](https://travis-ci.org/kata-containers/proxy.svg?branch=master)](https://travis-ci.org/kata-containers/proxy)
[![codecov](https://codecov.io/gh/kata-containers/proxy/branch/master/graph/badge.svg)](https://codecov.io/gh/kata-containers/proxy)

%package libexec
Summary: libexec components for the kata-proxy package.
Group: Default
Requires: kata-proxy-license = %{version}-%{release}

%description libexec
libexec components for the kata-proxy package.


%package license
Summary: license components for the kata-proxy package.
Group: Default

%description license
license components for the kata-proxy package.


%prep
%setup -q -n proxy-1.5.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1548264630
%autogen --disable-static ;export GOPATH="${PWD}/gopath/" \
;mkdir -p "${GOPATH}/src/github.com/kata-containers/" \
;ln -sf "${PWD}" "${GOPATH}/src/github.com/kata-containers/proxy" \
;cd "${GOPATH}/src/github.com/kata-containers/proxy"
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1548264630
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kata-proxy
cp LICENSE %{buildroot}/usr/share/package-licenses/kata-proxy/LICENSE
cp vendor/github.com/davecgh/go-spew/LICENSE %{buildroot}/usr/share/package-licenses/kata-proxy/vendor_github.com_davecgh_go-spew_LICENSE
cp vendor/github.com/hashicorp/yamux/LICENSE %{buildroot}/usr/share/package-licenses/kata-proxy/vendor_github.com_hashicorp_yamux_LICENSE
cp vendor/github.com/pmezard/go-difflib/LICENSE %{buildroot}/usr/share/package-licenses/kata-proxy/vendor_github.com_pmezard_go-difflib_LICENSE
cp vendor/github.com/sirupsen/logrus/LICENSE %{buildroot}/usr/share/package-licenses/kata-proxy/vendor_github.com_sirupsen_logrus_LICENSE
cp vendor/github.com/stretchr/testify/LICENSE %{buildroot}/usr/share/package-licenses/kata-proxy/vendor_github.com_stretchr_testify_LICENSE
cp vendor/golang.org/x/crypto/LICENSE %{buildroot}/usr/share/package-licenses/kata-proxy/vendor_golang.org_x_crypto_LICENSE
cp vendor/golang.org/x/sys/LICENSE %{buildroot}/usr/share/package-licenses/kata-proxy/vendor_golang.org_x_sys_LICENSE
%make_install

%files
%defattr(-,root,root,-)

%files libexec
%defattr(-,root,root,-)
/usr/libexec/kata-containers/kata-proxy

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kata-proxy/LICENSE
/usr/share/package-licenses/kata-proxy/vendor_github.com_davecgh_go-spew_LICENSE
/usr/share/package-licenses/kata-proxy/vendor_github.com_hashicorp_yamux_LICENSE
/usr/share/package-licenses/kata-proxy/vendor_github.com_pmezard_go-difflib_LICENSE
/usr/share/package-licenses/kata-proxy/vendor_github.com_sirupsen_logrus_LICENSE
/usr/share/package-licenses/kata-proxy/vendor_github.com_stretchr_testify_LICENSE
/usr/share/package-licenses/kata-proxy/vendor_golang.org_x_crypto_LICENSE
/usr/share/package-licenses/kata-proxy/vendor_golang.org_x_sys_LICENSE
