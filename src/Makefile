DUCKDB_DIR             ?= /duckdb
DUCKDB_AFLPLUSPLUS_DIR ?= /duckdb_aflplusplus

CC  ?= /AFLplusplus/afl-clang-fast
CXX ?= /AFLplusplus/afl-clang-fast++
CMAKE_VARS_BUILD ?=

DUCKDBLIB=$(DUCKDB_DIR)/build/release/src/libduckdb_static.a

DUCKDB_DEPS=$(DUCKDB_DIR)/build/release/third_party/fmt/libduckdb_fmt.a \
	$(DUCKDB_DIR)/build/release/third_party/libpg_query/libduckdb_pg_query.a \
	$(DUCKDB_DIR)/build/release/third_party/re2/libduckdb_re2.a \
	$(DUCKDB_DIR)/build/release/third_party/miniz/libduckdb_miniz.a \
	$(DUCKDB_DIR)/build/release/third_party/utf8proc/libduckdb_utf8proc.a \
	$(DUCKDB_DIR)/build/release/third_party/hyperloglog/libduckdb_hyperloglog.a \
	$(DUCKDB_DIR)/build/release/third_party/skiplist/libduckdb_skiplistlib.a \
	$(DUCKDB_DIR)/build/release/third_party/fastpforlib/libduckdb_fastpforlib.a \
	$(DUCKDB_DIR)/build/release/third_party/mbedtls/libduckdb_mbedtls.a \
	$(DUCKDB_DIR)/build/release/third_party/fsst/libduckdb_fsst.a \
	$(DUCKDB_DIR)/build/release/third_party/yyjson/libduckdb_yyjson.a \
	$(DUCKDB_DIR)/build/release/third_party/zstd/libduckdb_zstd.a

DUCKDB_EXT= $(DUCKDB_DIR)/build/release/extension/core_functions/libcore_functions_extension.a \
	$(DUCKDB_DIR)/build/release/extension/parquet/libparquet_extension.a \
	$(DUCKDB_DIR)/build/release/extension/json/libjson_extension.a

INC =-I$(DUCKDB_DIR)/src/include
CXXFLAGS = -std=c++11 -DDUCKDB_DIR=\"$(DUCKDB_DIR)\" -DDUCKDB_AFLPLUSPLUS_DIR=\"$(DUCKDB_AFLPLUSPLUS_DIR)\"

ifeq (${BUILD_JEMALLOC}, 1)
	CXXFLAGS:=${CXXFLAGS} -DBUILD_JEMALLOC=1
	DUCKDB_EXT:=${DUCKDB_EXT} $(DUCKDB_DIR)/build/release/extension/jemalloc/libjemalloc_extension.a
endif

ifeq (${USE_CCACHE}, 1)
	CMAKE_VARS_BUILD:=${CMAKE_VARS_BUILD} -DCCACHE_COMPILERCHECK=content
endif

duckdb-lib: $(DUCKDBLIB)

$(DUCKDBLIB):
	cd $(DUCKDB_DIR) && CC=$(CC) CXX=$(CXX) GEN=ninja BUILD_JSON=1 CRASH_ON_ASSERT=1 CMAKE_VARS_BUILD='$(CMAKE_VARS_BUILD)' make

.PHONY: all duckdb-lib
