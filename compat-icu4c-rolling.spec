#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v19
# autospec commit: a62a849
#
# Source0 file verified with key 0x4058F67406EAA6AB (ccornelius@google.com)
#
Name     : compat-icu4c-rolling
Version  : 73.2
Release  : 1
URL      : https://github.com/unicode-org/icu/releases/download/release-73-2/icu4c-73_2-src.tgz
Source0  : https://github.com/unicode-org/icu/releases/download/release-73-2/icu4c-73_2-src.tgz
Source1  : https://github.com/unicode-org/icu/releases/download/release-73-2/icu4c-73_2-src.tgz.asc
Source2  : 4058F67406EAA6AB.pkey
Summary  : International Components for Unicode
Group    : Development/Tools
License  : BSD-3-Clause ICU NCSA
Requires: compat-icu4c-rolling-lib = %{version}-%{release}
Requires: compat-icu4c-rolling-license = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : doxygen
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : gnupg
BuildRequires : pkg-config
BuildRequires : sed
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: backport-cal-fix.patch

%description
ICU is a set of C and C++ libraries that provides robust and full-featured
Unicode and locale support. The library provides calendar support, conversions
for many character sets, language sensitive collation, date
and time formatting, support for many locales, message catalogs
and resources, message formatting, normalization, number and currency
formatting, time zones support, transliteration, word, line and
sentence breaking, etc.

This package contains the Unicode character database and derived
properties, along with converters and time zones data.

This package contains the runtime libraries for ICU. It does
not contain any of the data files needed at runtime and present in the
`icu' and `icu-locales` packages.

%package lib
Summary: lib components for the compat-icu4c-rolling package.
Group: Libraries
Requires: compat-icu4c-rolling-license = %{version}-%{release}

%description lib
lib components for the compat-icu4c-rolling package.


%package lib32
Summary: lib32 components for the compat-icu4c-rolling package.
Group: Default
Requires: compat-icu4c-rolling-license = %{version}-%{release}

%description lib32
lib32 components for the compat-icu4c-rolling package.


%package license
Summary: license components for the compat-icu4c-rolling package.
Group: Default

%description license
license components for the compat-icu4c-rolling package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) 4058F67406EAA6AB' gpg.status
%setup -q -n icu
cd %{_builddir}/icu
%patch -P 1 -p1
pushd ..
cp -a icu build32
popd
pushd ..
cp -a icu buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1726255906
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
pushd source
export GOAMD64=v2
%configure --disable-static
make  %{?_smp_mflags}
popd

pushd ../build32/source
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/share/pkgconfig"
ASFLAGS="${CLEAR_INTERMEDIATE_ASFLAGS}${CLEAR_INTERMEDIATE_ASFLAGS:+ }--32"
CFLAGS="${CLEAR_INTERMEDIATE_CFLAGS}${CLEAR_INTERMEDIATE_CFLAGS:+ }-m32 -mstackrealign"
CXXFLAGS="${CLEAR_INTERMEDIATE_CXXFLAGS}${CLEAR_INTERMEDIATE_CXXFLAGS:+ }-m32 -mstackrealign"
LDFLAGS="${CLEAR_INTERMEDIATE_LDFLAGS}${CLEAR_INTERMEDIATE_LDFLAGS:+ }-m32 -mstackrealign"
%configure --disable-static    --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
unset PKG_CONFIG_PATH
pushd ../buildavx2/source
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure --disable-static
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
pushd source; make %{?_smp_mflags} check; popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1726255906
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/compat-icu4c-rolling
cp %{_builddir}/icu/LICENSE %{buildroot}/usr/share/package-licenses/compat-icu4c-rolling/68693549ac10f254414f549cb11901d27da3220b || :
cp %{_builddir}/icu/license.html %{buildroot}/usr/share/package-licenses/compat-icu4c-rolling/06e7821c4127e21850f5c981698443b6f31e0ef1 || :
export GOAMD64=v2
pushd ../build32/source
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
if [ -d %{buildroot}/usr/share/pkgconfig ]
then
pushd %{buildroot}/usr/share/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
GOAMD64=v3
pushd ../buildavx2/source
%make_install_v3
popd
pushd source
GOAMD64=v2
%make_install
popd
## Remove excluded files
rm -f %{buildroot}*/V3/usr/bin/derb
rm -f %{buildroot}*/V3/usr/bin/escapesrc
rm -f %{buildroot}*/V3/usr/bin/genbrk
rm -f %{buildroot}*/V3/usr/bin/genccode
rm -f %{buildroot}*/V3/usr/bin/gencfu
rm -f %{buildroot}*/V3/usr/bin/gencmn
rm -f %{buildroot}*/V3/usr/bin/gencnval
rm -f %{buildroot}*/V3/usr/bin/gendict
rm -f %{buildroot}*/V3/usr/bin/gennorm2
rm -f %{buildroot}*/V3/usr/bin/genrb
rm -f %{buildroot}*/V3/usr/bin/gensprep
rm -f %{buildroot}*/V3/usr/bin/icuexportdata
rm -f %{buildroot}*/V3/usr/bin/icuinfo
rm -f %{buildroot}*/V3/usr/bin/icupkg
rm -f %{buildroot}*/V3/usr/bin/makeconv
rm -f %{buildroot}*/V3/usr/bin/pkgdata
rm -f %{buildroot}*/V3/usr/bin/uconv
rm -f %{buildroot}*/usr/bin/derb
rm -f %{buildroot}*/usr/bin/escapesrc
rm -f %{buildroot}*/usr/bin/genbrk
rm -f %{buildroot}*/usr/bin/genccode
rm -f %{buildroot}*/usr/bin/gencfu
rm -f %{buildroot}*/usr/bin/gencmn
rm -f %{buildroot}*/usr/bin/gencnval
rm -f %{buildroot}*/usr/bin/gendict
rm -f %{buildroot}*/usr/bin/gennorm2
rm -f %{buildroot}*/usr/bin/genrb
rm -f %{buildroot}*/usr/bin/gensprep
rm -f %{buildroot}*/usr/bin/icu-config
rm -f %{buildroot}*/usr/bin/icuexportdata
rm -f %{buildroot}*/usr/bin/icuinfo
rm -f %{buildroot}*/usr/bin/icupkg
rm -f %{buildroot}*/usr/bin/makeconv
rm -f %{buildroot}*/usr/bin/pkgdata
rm -f %{buildroot}*/usr/bin/uconv
rm -f %{buildroot}*/usr/include/unicode/alphaindex.h
rm -f %{buildroot}*/usr/include/unicode/appendable.h
rm -f %{buildroot}*/usr/include/unicode/basictz.h
rm -f %{buildroot}*/usr/include/unicode/brkiter.h
rm -f %{buildroot}*/usr/include/unicode/bytestream.h
rm -f %{buildroot}*/usr/include/unicode/bytestrie.h
rm -f %{buildroot}*/usr/include/unicode/bytestriebuilder.h
rm -f %{buildroot}*/usr/include/unicode/calendar.h
rm -f %{buildroot}*/usr/include/unicode/caniter.h
rm -f %{buildroot}*/usr/include/unicode/casemap.h
rm -f %{buildroot}*/usr/include/unicode/char16ptr.h
rm -f %{buildroot}*/usr/include/unicode/chariter.h
rm -f %{buildroot}*/usr/include/unicode/choicfmt.h
rm -f %{buildroot}*/usr/include/unicode/coleitr.h
rm -f %{buildroot}*/usr/include/unicode/coll.h
rm -f %{buildroot}*/usr/include/unicode/compactdecimalformat.h
rm -f %{buildroot}*/usr/include/unicode/curramt.h
rm -f %{buildroot}*/usr/include/unicode/currpinf.h
rm -f %{buildroot}*/usr/include/unicode/currunit.h
rm -f %{buildroot}*/usr/include/unicode/datefmt.h
rm -f %{buildroot}*/usr/include/unicode/dbbi.h
rm -f %{buildroot}*/usr/include/unicode/dcfmtsym.h
rm -f %{buildroot}*/usr/include/unicode/decimfmt.h
rm -f %{buildroot}*/usr/include/unicode/displayoptions.h
rm -f %{buildroot}*/usr/include/unicode/docmain.h
rm -f %{buildroot}*/usr/include/unicode/dtfmtsym.h
rm -f %{buildroot}*/usr/include/unicode/dtintrv.h
rm -f %{buildroot}*/usr/include/unicode/dtitvfmt.h
rm -f %{buildroot}*/usr/include/unicode/dtitvinf.h
rm -f %{buildroot}*/usr/include/unicode/dtptngen.h
rm -f %{buildroot}*/usr/include/unicode/dtrule.h
rm -f %{buildroot}*/usr/include/unicode/edits.h
rm -f %{buildroot}*/usr/include/unicode/enumset.h
rm -f %{buildroot}*/usr/include/unicode/errorcode.h
rm -f %{buildroot}*/usr/include/unicode/fieldpos.h
rm -f %{buildroot}*/usr/include/unicode/filteredbrk.h
rm -f %{buildroot}*/usr/include/unicode/fmtable.h
rm -f %{buildroot}*/usr/include/unicode/format.h
rm -f %{buildroot}*/usr/include/unicode/formattednumber.h
rm -f %{buildroot}*/usr/include/unicode/formattedvalue.h
rm -f %{buildroot}*/usr/include/unicode/fpositer.h
rm -f %{buildroot}*/usr/include/unicode/gender.h
rm -f %{buildroot}*/usr/include/unicode/gregocal.h
rm -f %{buildroot}*/usr/include/unicode/icudataver.h
rm -f %{buildroot}*/usr/include/unicode/icuplug.h
rm -f %{buildroot}*/usr/include/unicode/idna.h
rm -f %{buildroot}*/usr/include/unicode/listformatter.h
rm -f %{buildroot}*/usr/include/unicode/localebuilder.h
rm -f %{buildroot}*/usr/include/unicode/localematcher.h
rm -f %{buildroot}*/usr/include/unicode/localpointer.h
rm -f %{buildroot}*/usr/include/unicode/locdspnm.h
rm -f %{buildroot}*/usr/include/unicode/locid.h
rm -f %{buildroot}*/usr/include/unicode/measfmt.h
rm -f %{buildroot}*/usr/include/unicode/measunit.h
rm -f %{buildroot}*/usr/include/unicode/measure.h
rm -f %{buildroot}*/usr/include/unicode/messagepattern.h
rm -f %{buildroot}*/usr/include/unicode/msgfmt.h
rm -f %{buildroot}*/usr/include/unicode/normalizer2.h
rm -f %{buildroot}*/usr/include/unicode/normlzr.h
rm -f %{buildroot}*/usr/include/unicode/nounit.h
rm -f %{buildroot}*/usr/include/unicode/numberformatter.h
rm -f %{buildroot}*/usr/include/unicode/numberrangeformatter.h
rm -f %{buildroot}*/usr/include/unicode/numfmt.h
rm -f %{buildroot}*/usr/include/unicode/numsys.h
rm -f %{buildroot}*/usr/include/unicode/parseerr.h
rm -f %{buildroot}*/usr/include/unicode/parsepos.h
rm -f %{buildroot}*/usr/include/unicode/platform.h
rm -f %{buildroot}*/usr/include/unicode/plurfmt.h
rm -f %{buildroot}*/usr/include/unicode/plurrule.h
rm -f %{buildroot}*/usr/include/unicode/ptypes.h
rm -f %{buildroot}*/usr/include/unicode/putil.h
rm -f %{buildroot}*/usr/include/unicode/rbbi.h
rm -f %{buildroot}*/usr/include/unicode/rbnf.h
rm -f %{buildroot}*/usr/include/unicode/rbtz.h
rm -f %{buildroot}*/usr/include/unicode/regex.h
rm -f %{buildroot}*/usr/include/unicode/region.h
rm -f %{buildroot}*/usr/include/unicode/reldatefmt.h
rm -f %{buildroot}*/usr/include/unicode/rep.h
rm -f %{buildroot}*/usr/include/unicode/resbund.h
rm -f %{buildroot}*/usr/include/unicode/schriter.h
rm -f %{buildroot}*/usr/include/unicode/scientificnumberformatter.h
rm -f %{buildroot}*/usr/include/unicode/search.h
rm -f %{buildroot}*/usr/include/unicode/selfmt.h
rm -f %{buildroot}*/usr/include/unicode/simpleformatter.h
rm -f %{buildroot}*/usr/include/unicode/simplenumberformatter.h
rm -f %{buildroot}*/usr/include/unicode/simpletz.h
rm -f %{buildroot}*/usr/include/unicode/smpdtfmt.h
rm -f %{buildroot}*/usr/include/unicode/sortkey.h
rm -f %{buildroot}*/usr/include/unicode/std_string.h
rm -f %{buildroot}*/usr/include/unicode/strenum.h
rm -f %{buildroot}*/usr/include/unicode/stringoptions.h
rm -f %{buildroot}*/usr/include/unicode/stringpiece.h
rm -f %{buildroot}*/usr/include/unicode/stringtriebuilder.h
rm -f %{buildroot}*/usr/include/unicode/stsearch.h
rm -f %{buildroot}*/usr/include/unicode/symtable.h
rm -f %{buildroot}*/usr/include/unicode/tblcoll.h
rm -f %{buildroot}*/usr/include/unicode/timezone.h
rm -f %{buildroot}*/usr/include/unicode/tmunit.h
rm -f %{buildroot}*/usr/include/unicode/tmutamt.h
rm -f %{buildroot}*/usr/include/unicode/tmutfmt.h
rm -f %{buildroot}*/usr/include/unicode/translit.h
rm -f %{buildroot}*/usr/include/unicode/tzfmt.h
rm -f %{buildroot}*/usr/include/unicode/tznames.h
rm -f %{buildroot}*/usr/include/unicode/tzrule.h
rm -f %{buildroot}*/usr/include/unicode/tztrans.h
rm -f %{buildroot}*/usr/include/unicode/ubidi.h
rm -f %{buildroot}*/usr/include/unicode/ubiditransform.h
rm -f %{buildroot}*/usr/include/unicode/ubrk.h
rm -f %{buildroot}*/usr/include/unicode/ucal.h
rm -f %{buildroot}*/usr/include/unicode/ucasemap.h
rm -f %{buildroot}*/usr/include/unicode/ucat.h
rm -f %{buildroot}*/usr/include/unicode/uchar.h
rm -f %{buildroot}*/usr/include/unicode/ucharstrie.h
rm -f %{buildroot}*/usr/include/unicode/ucharstriebuilder.h
rm -f %{buildroot}*/usr/include/unicode/uchriter.h
rm -f %{buildroot}*/usr/include/unicode/uclean.h
rm -f %{buildroot}*/usr/include/unicode/ucnv.h
rm -f %{buildroot}*/usr/include/unicode/ucnv_cb.h
rm -f %{buildroot}*/usr/include/unicode/ucnv_err.h
rm -f %{buildroot}*/usr/include/unicode/ucnvsel.h
rm -f %{buildroot}*/usr/include/unicode/ucol.h
rm -f %{buildroot}*/usr/include/unicode/ucoleitr.h
rm -f %{buildroot}*/usr/include/unicode/uconfig.h
rm -f %{buildroot}*/usr/include/unicode/ucpmap.h
rm -f %{buildroot}*/usr/include/unicode/ucptrie.h
rm -f %{buildroot}*/usr/include/unicode/ucsdet.h
rm -f %{buildroot}*/usr/include/unicode/ucurr.h
rm -f %{buildroot}*/usr/include/unicode/udat.h
rm -f %{buildroot}*/usr/include/unicode/udata.h
rm -f %{buildroot}*/usr/include/unicode/udateintervalformat.h
rm -f %{buildroot}*/usr/include/unicode/udatpg.h
rm -f %{buildroot}*/usr/include/unicode/udisplaycontext.h
rm -f %{buildroot}*/usr/include/unicode/udisplayoptions.h
rm -f %{buildroot}*/usr/include/unicode/uenum.h
rm -f %{buildroot}*/usr/include/unicode/ufieldpositer.h
rm -f %{buildroot}*/usr/include/unicode/uformattable.h
rm -f %{buildroot}*/usr/include/unicode/uformattednumber.h
rm -f %{buildroot}*/usr/include/unicode/uformattedvalue.h
rm -f %{buildroot}*/usr/include/unicode/ugender.h
rm -f %{buildroot}*/usr/include/unicode/uidna.h
rm -f %{buildroot}*/usr/include/unicode/uiter.h
rm -f %{buildroot}*/usr/include/unicode/uldnames.h
rm -f %{buildroot}*/usr/include/unicode/ulistformatter.h
rm -f %{buildroot}*/usr/include/unicode/uloc.h
rm -f %{buildroot}*/usr/include/unicode/ulocdata.h
rm -f %{buildroot}*/usr/include/unicode/umachine.h
rm -f %{buildroot}*/usr/include/unicode/umisc.h
rm -f %{buildroot}*/usr/include/unicode/umsg.h
rm -f %{buildroot}*/usr/include/unicode/umutablecptrie.h
rm -f %{buildroot}*/usr/include/unicode/unifilt.h
rm -f %{buildroot}*/usr/include/unicode/unifunct.h
rm -f %{buildroot}*/usr/include/unicode/unimatch.h
rm -f %{buildroot}*/usr/include/unicode/unirepl.h
rm -f %{buildroot}*/usr/include/unicode/uniset.h
rm -f %{buildroot}*/usr/include/unicode/unistr.h
rm -f %{buildroot}*/usr/include/unicode/unorm.h
rm -f %{buildroot}*/usr/include/unicode/unorm2.h
rm -f %{buildroot}*/usr/include/unicode/unum.h
rm -f %{buildroot}*/usr/include/unicode/unumberformatter.h
rm -f %{buildroot}*/usr/include/unicode/unumberoptions.h
rm -f %{buildroot}*/usr/include/unicode/unumberrangeformatter.h
rm -f %{buildroot}*/usr/include/unicode/unumsys.h
rm -f %{buildroot}*/usr/include/unicode/uobject.h
rm -f %{buildroot}*/usr/include/unicode/upluralrules.h
rm -f %{buildroot}*/usr/include/unicode/uregex.h
rm -f %{buildroot}*/usr/include/unicode/uregion.h
rm -f %{buildroot}*/usr/include/unicode/ureldatefmt.h
rm -f %{buildroot}*/usr/include/unicode/urename.h
rm -f %{buildroot}*/usr/include/unicode/urep.h
rm -f %{buildroot}*/usr/include/unicode/ures.h
rm -f %{buildroot}*/usr/include/unicode/uscript.h
rm -f %{buildroot}*/usr/include/unicode/usearch.h
rm -f %{buildroot}*/usr/include/unicode/uset.h
rm -f %{buildroot}*/usr/include/unicode/usetiter.h
rm -f %{buildroot}*/usr/include/unicode/ushape.h
rm -f %{buildroot}*/usr/include/unicode/usimplenumberformatter.h
rm -f %{buildroot}*/usr/include/unicode/uspoof.h
rm -f %{buildroot}*/usr/include/unicode/usprep.h
rm -f %{buildroot}*/usr/include/unicode/ustdio.h
rm -f %{buildroot}*/usr/include/unicode/ustream.h
rm -f %{buildroot}*/usr/include/unicode/ustring.h
rm -f %{buildroot}*/usr/include/unicode/ustringtrie.h
rm -f %{buildroot}*/usr/include/unicode/utext.h
rm -f %{buildroot}*/usr/include/unicode/utf.h
rm -f %{buildroot}*/usr/include/unicode/utf16.h
rm -f %{buildroot}*/usr/include/unicode/utf32.h
rm -f %{buildroot}*/usr/include/unicode/utf8.h
rm -f %{buildroot}*/usr/include/unicode/utf_old.h
rm -f %{buildroot}*/usr/include/unicode/utmscale.h
rm -f %{buildroot}*/usr/include/unicode/utrace.h
rm -f %{buildroot}*/usr/include/unicode/utrans.h
rm -f %{buildroot}*/usr/include/unicode/utypes.h
rm -f %{buildroot}*/usr/include/unicode/uvernum.h
rm -f %{buildroot}*/usr/include/unicode/uversion.h
rm -f %{buildroot}*/usr/include/unicode/vtzone.h
rm -f %{buildroot}*/usr/lib32/icu/73.2/Makefile.inc
rm -f %{buildroot}*/usr/lib32/icu/73.2/pkgdata.inc
rm -f %{buildroot}*/usr/lib32/icu/Makefile.inc
rm -f %{buildroot}*/usr/lib32/icu/current
rm -f %{buildroot}*/usr/lib32/icu/pkgdata.inc
rm -f %{buildroot}*/usr/lib32/libicudata.so
rm -f %{buildroot}*/usr/lib32/libicui18n.so
rm -f %{buildroot}*/usr/lib32/libicuio.so
rm -f %{buildroot}*/usr/lib32/libicutest.so
rm -f %{buildroot}*/usr/lib32/libicutu.so
rm -f %{buildroot}*/usr/lib32/libicuuc.so
rm -f %{buildroot}*/usr/lib32/pkgconfig/32icu-i18n.pc
rm -f %{buildroot}*/usr/lib32/pkgconfig/32icu-io.pc
rm -f %{buildroot}*/usr/lib32/pkgconfig/32icu-uc.pc
rm -f %{buildroot}*/usr/lib32/pkgconfig/icu-i18n.pc
rm -f %{buildroot}*/usr/lib32/pkgconfig/icu-io.pc
rm -f %{buildroot}*/usr/lib32/pkgconfig/icu-uc.pc
rm -f %{buildroot}*/usr/lib64/icu/73.2/Makefile.inc
rm -f %{buildroot}*/usr/lib64/icu/73.2/pkgdata.inc
rm -f %{buildroot}*/usr/lib64/icu/Makefile.inc
rm -f %{buildroot}*/usr/lib64/icu/current
rm -f %{buildroot}*/usr/lib64/icu/pkgdata.inc
rm -f %{buildroot}*/usr/lib64/libicudata.so
rm -f %{buildroot}*/usr/lib64/libicui18n.so
rm -f %{buildroot}*/usr/lib64/libicuio.so
rm -f %{buildroot}*/usr/lib64/libicutest.so
rm -f %{buildroot}*/usr/lib64/libicutu.so
rm -f %{buildroot}*/usr/lib64/libicuuc.so
rm -f %{buildroot}*/usr/lib64/pkgconfig/icu-i18n.pc
rm -f %{buildroot}*/usr/lib64/pkgconfig/icu-io.pc
rm -f %{buildroot}*/usr/lib64/pkgconfig/icu-uc.pc
rm -f %{buildroot}*/usr/share/icu/73.2/LICENSE
rm -f %{buildroot}*/usr/share/icu/73.2/config/mh-linux
rm -f %{buildroot}*/usr/share/icu/73.2/install-sh
rm -f %{buildroot}*/usr/share/icu/73.2/mkinstalldirs
rm -f %{buildroot}*/usr/share/man/man1/derb.1
rm -f %{buildroot}*/usr/share/man/man1/genbrk.1
rm -f %{buildroot}*/usr/share/man/man1/gencfu.1
rm -f %{buildroot}*/usr/share/man/man1/gencnval.1
rm -f %{buildroot}*/usr/share/man/man1/gendict.1
rm -f %{buildroot}*/usr/share/man/man1/genrb.1
rm -f %{buildroot}*/usr/share/man/man1/icu-config.1
rm -f %{buildroot}*/usr/share/man/man1/icuexportdata.1
rm -f %{buildroot}*/usr/share/man/man1/makeconv.1
rm -f %{buildroot}*/usr/share/man/man1/pkgdata.1
rm -f %{buildroot}*/usr/share/man/man1/uconv.1
rm -f %{buildroot}*/usr/share/man/man8/genccode.8
rm -f %{buildroot}*/usr/share/man/man8/gencmn.8
rm -f %{buildroot}*/usr/share/man/man8/gensprep.8
rm -f %{buildroot}*/usr/share/man/man8/icupkg.8
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libicudata.so.73.2
/V3/usr/lib64/libicui18n.so.73.2
/V3/usr/lib64/libicuio.so.73.2
/V3/usr/lib64/libicutest.so.73.2
/V3/usr/lib64/libicutu.so.73.2
/V3/usr/lib64/libicuuc.so.73.2
/usr/lib64/libicudata.so.73
/usr/lib64/libicudata.so.73.2
/usr/lib64/libicui18n.so.73
/usr/lib64/libicui18n.so.73.2
/usr/lib64/libicuio.so.73
/usr/lib64/libicuio.so.73.2
/usr/lib64/libicutest.so.73
/usr/lib64/libicutest.so.73.2
/usr/lib64/libicutu.so.73
/usr/lib64/libicutu.so.73.2
/usr/lib64/libicuuc.so.73
/usr/lib64/libicuuc.so.73.2

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libicudata.so.73
/usr/lib32/libicudata.so.73.2
/usr/lib32/libicui18n.so.73
/usr/lib32/libicui18n.so.73.2
/usr/lib32/libicuio.so.73
/usr/lib32/libicuio.so.73.2
/usr/lib32/libicutest.so.73
/usr/lib32/libicutest.so.73.2
/usr/lib32/libicutu.so.73
/usr/lib32/libicutu.so.73.2
/usr/lib32/libicuuc.so.73
/usr/lib32/libicuuc.so.73.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/compat-icu4c-rolling/06e7821c4127e21850f5c981698443b6f31e0ef1
/usr/share/package-licenses/compat-icu4c-rolling/68693549ac10f254414f549cb11901d27da3220b
