cmake_minimum_required(VERSION 3.0)

project(FreeImage)

option(BUILD_SHARED_LIBS "Build FreeImage as a shared library" OFF)

if(BUILD_SHARED_LIBS)
    message(STATUS "Building FreeImage as a shared library.")
    # If building as a shared library, do not define FREEIMAGE_LIB
else()
    message(STATUS "Building FreeImage as a static library.")
    add_definitions(-DFREEIMAGE_LIB)
endif()

message("BUILD_OPENEXR foo: ${BUILD_OPENEXR}")

if(${NO_BUILD_ZLIB}) 
    message("BUILD_ZLIB = FALSE")
else()
    set(BUILD_ZLIB 1)
endif()

if(${NO_BUILD_JXR}) 
    message("BUILD_JXR = FALSE")
else()
    set(BUILD_JXR 1)
endif()

if(${NO_BUILD_WEBP}) 
    message("BUILD_WEBP = FALSE")
else()
    set(BUILD_WEBP 1)
endif()

if(${NO_BUILD_LIBRAWLITE}) 
    message("BUILD_LIBRAWLITE = FALSE")
else()
    set(BUILD_LIBRAWLITE 1)
endif()


if(${NO_BUILD_OPENEXR}) 
    message("BUILD_OPENEXR = FALSE")
else()
    set(BUILD_OPENEXR 1)
endif()

if(${NO_BUILD_LIBTIFF}) 
    message("BUILD_LIBTIFF = FALSE")
else()
    set(BUILD_LIBTIFF 1)
endif()

set(FreeImage_SOURCES
    ./Source/FreeImage/BitmapAccess.cpp ./Source/FreeImage/ColorLookup.cpp ./Source/FreeImage/ConversionRGBA16.cpp ./Source/FreeImage/ConversionRGBAF.cpp ./Source/FreeImage/FreeImage.cpp ./Source/FreeImage/FreeImageC.c ./Source/FreeImage/FreeImageIO.cpp ./Source/FreeImage/GetType.cpp ./Source/FreeImage/LFPQuantizer.cpp ./Source/FreeImage/MemoryIO.cpp ./Source/FreeImage/PixelAccess.cpp ./Source/FreeImage/J2KHelper.cpp ./Source/FreeImage/MNGHelper.cpp ./Source/FreeImage/Plugin.cpp ./Source/FreeImage/PluginBMP.cpp ./Source/FreeImage/PluginCUT.cpp ./Source/FreeImage/PluginDDS.cpp ./Source/FreeImage/PluginEXR.cpp ./Source/FreeImage/PluginG3.cpp ./Source/FreeImage/PluginGIF.cpp ./Source/FreeImage/PluginHDR.cpp ./Source/FreeImage/PluginICO.cpp ./Source/FreeImage/PluginIFF.cpp ./Source/FreeImage/PluginJ2K.cpp ./Source/FreeImage/PluginJNG.cpp ./Source/FreeImage/PluginJP2.cpp ./Source/FreeImage/PluginJPEG.cpp  ./Source/FreeImage/PluginKOALA.cpp ./Source/FreeImage/PluginMNG.cpp ./Source/FreeImage/PluginPCD.cpp ./Source/FreeImage/PluginPCX.cpp ./Source/FreeImage/PluginPFM.cpp ./Source/FreeImage/PluginPICT.cpp ./Source/FreeImage/PluginPNG.cpp ./Source/FreeImage/PluginPNM.cpp ./Source/FreeImage/PluginPSD.cpp ./Source/FreeImage/PluginRAS.cpp ./Source/FreeImage/PluginRAW.cpp ./Source/FreeImage/PluginSGI.cpp ./Source/FreeImage/PluginTARGA.cpp ./Source/FreeImage/PluginTIFF.cpp ./Source/FreeImage/PluginWBMP.cpp ./Source/FreeImage/PluginWebP.cpp ./Source/FreeImage/PluginXBM.cpp ./Source/FreeImage/PluginXPM.cpp ./Source/FreeImage/PSDParser.cpp ./Source/FreeImage/TIFFLogLuv.cpp ./Source/FreeImage/Conversion.cpp ./Source/FreeImage/Conversion16_555.cpp ./Source/FreeImage/Conversion16_565.cpp ./Source/FreeImage/Conversion24.cpp ./Source/FreeImage/Conversion32.cpp ./Source/FreeImage/Conversion4.cpp ./Source/FreeImage/Conversion8.cpp ./Source/FreeImage/ConversionFloat.cpp ./Source/FreeImage/ConversionRGB16.cpp ./Source/FreeImage/ConversionRGBF.cpp ./Source/FreeImage/ConversionType.cpp ./Source/FreeImage/ConversionUINT16.cpp ./Source/FreeImage/Halftoning.cpp ./Source/FreeImage/tmoColorConvert.cpp ./Source/FreeImage/tmoDrago03.cpp ./Source/FreeImage/tmoFattal02.cpp ./Source/FreeImage/tmoReinhard05.cpp ./Source/FreeImage/ToneMapping.cpp ./Source/FreeImage/NNQuantizer.cpp ./Source/FreeImage/WuQuantizer.cpp ./Source/FreeImage/CacheFile.cpp ./Source/FreeImage/MultiPage.cpp ./Source/FreeImage/ZLibInterface.cpp ./Source/Metadata/Exif.cpp ./Source/Metadata/FIRational.cpp ./Source/Metadata/FreeImageTag.cpp ./Source/Metadata/IPTC.cpp ./Source/Metadata/TagConversion.cpp ./Source/Metadata/TagLib.cpp ./Source/Metadata/XTIFF.cpp ./Source/FreeImageToolkit/Background.cpp ./Source/FreeImageToolkit/BSplineRotate.cpp ./Source/FreeImageToolkit/Channels.cpp ./Source/FreeImageToolkit/ClassicRotate.cpp ./Source/FreeImageToolkit/Colors.cpp ./Source/FreeImageToolkit/CopyPaste.cpp ./Source/FreeImageToolkit/Display.cpp ./Source/FreeImageToolkit/Flip.cpp ./Source/FreeImageToolkit/JPEGTransform.cpp ./Source/FreeImageToolkit/MultigridPoissonSolver.cpp ./Source/FreeImageToolkit/Rescale.cpp ./Source/FreeImageToolkit/Resize.cpp Source/LibJPEG/jaricom.c Source/LibJPEG/jcapimin.c Source/LibJPEG/jcapistd.c Source/LibJPEG/jcarith.c Source/LibJPEG/jccoefct.c Source/LibJPEG/jccolor.c Source/LibJPEG/jcdctmgr.c Source/LibJPEG/jchuff.c Source/LibJPEG/jcinit.c Source/LibJPEG/jcmainct.c Source/LibJPEG/jcmarker.c Source/LibJPEG/jcmaster.c Source/LibJPEG/jcomapi.c Source/LibJPEG/jcparam.c Source/LibJPEG/jcprepct.c Source/LibJPEG/jcsample.c Source/LibJPEG/jctrans.c Source/LibJPEG/jdapimin.c Source/LibJPEG/jdapistd.c Source/LibJPEG/jdarith.c Source/LibJPEG/jdatadst.c Source/LibJPEG/jdatasrc.c Source/LibJPEG/jdcoefct.c Source/LibJPEG/jdcolor.c Source/LibJPEG/jddctmgr.c Source/LibJPEG/jdhuff.c Source/LibJPEG/jdinput.c Source/LibJPEG/jdmainct.c Source/LibJPEG/jdmarker.c Source/LibJPEG/jdmaster.c Source/LibJPEG/jdmerge.c Source/LibJPEG/jdpostct.c Source/LibJPEG/jdsample.c Source/LibJPEG/jdtrans.c Source/LibJPEG/jerror.c Source/LibJPEG/jfdctflt.c Source/LibJPEG/jfdctfst.c Source/LibJPEG/jfdctint.c Source/LibJPEG/jidctflt.c Source/LibJPEG/jidctfst.c Source/LibJPEG/jidctint.c Source/LibJPEG/jmemmgr.c Source/LibJPEG/jmemnobs.c Source/LibJPEG/jquant1.c Source/LibJPEG/jquant2.c Source/LibJPEG/jutils.c Source/LibJPEG/transupp.c Source/LibOpenJPEG/bio.c Source/LibOpenJPEG/cio.c Source/LibOpenJPEG/dwt.c Source/LibOpenJPEG/event.c Source/LibOpenJPEG/function_list.c Source/LibOpenJPEG/image.c Source/LibOpenJPEG/invert.c Source/LibOpenJPEG/j2k.c Source/LibOpenJPEG/jp2.c Source/LibOpenJPEG/mct.c Source/LibOpenJPEG/mqc.c Source/LibOpenJPEG/openjpeg.c Source/LibOpenJPEG/opj_clock.c Source/LibOpenJPEG/pi.c Source/LibOpenJPEG/raw.c Source/LibOpenJPEG/t1.c Source/LibOpenJPEG/t2.c Source/LibOpenJPEG/tcd.c Source/LibOpenJPEG/tgt.c ./Source/CacheFile.h ./Source/FreeImage ./Source/FreeImage.h ./Source/FreeImageIO.h ./Source/LibJPEG/cderror.h ./Source/LibJPEG/cdjpeg.h ./Source/LibJPEG/jconfig.h ./Source/LibJPEG/jdct.h ./Source/LibJPEG/jerror.h ./Source/LibJPEG/jinclude.h ./Source/LibJPEG/jpegint.h ./Source/LibJPEG/jpeglib.h ./Source/LibJPEG/jmemsys.h ./Source/LibJPEG/jmorecfg.h ./Source/LibJPEG/transupp.h ./Source/LibJPEG/jversion.h ./Source/LibOpenJPEG/bio.c ./Source/LibOpenJPEG/cio.c ./Source/LibOpenJPEG/dwt.c ./Source/LibOpenJPEG/event.c ./Source/LibOpenJPEG/function_list.c ./Source/LibOpenJPEG/image.c ./Source/LibOpenJPEG/invert.c ./Source/LibOpenJPEG/j2k.c ./Source/LibOpenJPEG/jp2.c ./Source/LibOpenJPEG/mct.c ./Source/LibOpenJPEG/mqc.c ./Source/LibOpenJPEG/openjpeg.c ./Source/LibOpenJPEG/opj_clock.c ./Source/LibOpenJPEG/pi.c ./Source/LibOpenJPEG/raw.c ./Source/LibOpenJPEG/t1.c ./Source/LibOpenJPEG/t2.c ./Source/LibOpenJPEG/tcd.c ./Source/LibOpenJPEG/tgt.c ./Source/MapIntrospector.h ./Source/Metadata/FIRational.h ./Source/Metadata/FreeImageTag.h ./Source/Plugin.h ./Source/Quantizers.h ./Source/ToneMapping.h ./Source/Utilities.h ./TestAPI/TestSuite.h  
)

if(BUILD_LIBPNG) 
set(FreeImage_LIBPNG_SRCS
Source/LibPNG/png.c Source/LibPNG/pngerror.c Source/LibPNG/pngget.c Source/LibPNG/pngmem.c Source/LibPNG/pngpread.c Source/LibPNG/pngread.c Source/LibPNG/pngrio.c Source/LibPNG/pngrtran.c Source/LibPNG/pngrutil.c Source/LibPNG/pngset.c Source/LibPNG/pngtrans.c Source/LibPNG/pngwio.c Source/LibPNG/pngwrite.c Source/LibPNG/pngwtran.c Source/LibPNG/pngwutil.c
./Source/LibPNG/png.h ./Source/LibPNG/pngconf.h ./Source/LibPNG/pngdebug.h ./Source/LibPNG/pnginfo.h ./Source/LibPNG/pnglibconf.h ./Source/LibPNG/pngpriv.h ./Source/LibPNG/pngstruct.h
)
endif()


include_directories(${PNG_INCLUDE_DIR})
list(APPEND FreeImage_LIBTIFF_SRCS ${PNG_LIBRARY})

if(BUILD_LIBTIFF)
set(FreeImage_LIBTIFF_SRCS 
Source/LibTIFF4/mkg3states.c           Source/LibTIFF4/tif_error.c
Source/LibTIFF4/tif_aux.c              Source/LibTIFF4/tif_close.c
Source/LibTIFF4/tif_codec.c            Source/LibTIFF4/tif_color.c
Source/LibTIFF4/tif_compress.c         Source/LibTIFF4/tif_config.h
Source/LibTIFF4/tif_config.vc.h        Source/LibTIFF4/tif_config.wince.h
Source/LibTIFF4/tif_config.wince.h     Source/LibTIFF4/tif_dir.c
Source/LibTIFF4/tif_dir.h              Source/LibTIFF4/tif_dirinfo.c
Source/LibTIFF4/tif_dirread.c          Source/LibTIFF4/tif_dirwrite.c
Source/LibTIFF4/tif_dumpmode.c         Source/LibTIFF4/tif_error.c
Source/LibTIFF4/tif_extension.c        Source/LibTIFF4/tif_fax3.c
Source/LibTIFF4/tif_fax3.h             Source/LibTIFF4/tif_fax3sm.c
Source/LibTIFF4/tif_flush.c            Source/LibTIFF4/tif_getimage.c
Source/LibTIFF4/tif_hash_set.c         Source/LibTIFF4/tif_hash_set.h
Source/LibTIFF4/tif_jbig.c             Source/LibTIFF4/tif_jpeg.c
Source/LibTIFF4/tif_jpeg_12.c          Source/LibTIFF4/tif_lerc.c
Source/LibTIFF4/tif_luv.c              Source/LibTIFF4/tif_lzw.c
Source/LibTIFF4/tif_lzw.c              Source/LibTIFF4/tif_next.c
Source/LibTIFF4/tif_ojpeg.c            Source/LibTIFF4/tif_open.c
Source/LibTIFF4/tif_packbits.c         Source/LibTIFF4/tif_pixarlog.c
Source/LibTIFF4/tif_predict.c          Source/LibTIFF4/tif_predict.h
Source/LibTIFF4/tif_print.c            Source/LibTIFF4/tif_read.c
Source/LibTIFF4/tif_strip.c            Source/LibTIFF4/tif_swab.c
Source/LibTIFF4/tif_thunder.c          Source/LibTIFF4/tif_tile.c
Source/LibTIFF4/tif_version.c          Source/LibTIFF4/tif_warning.c
Source/LibTIFF4/tif_webp.c             Source/LibTIFF4/tif_write.c   
Source/LibTIFF4/tif_zip.c              Source/LibTIFF4/tif_zstd.c
Source/LibTIFF4/tiff.h                 Source/LibTIFF4/tiffconf.h
Source/LibTIFF4/tiffconf.vc.h          Source/LibTIFF4/tiffconf.wince.h
Source/LibTIFF4/tiffio.h               Source/LibTIFF4/tiffiop.h
Source/LibTIFF4/tiffvers.h             Source/LibTIFF4/uvcode.h
Source/LibTIFF4/t4.h                   Source/LibTIFF4/libport.h
)
# Add Windows-specific source files if building on Windows
if(WIN32)
    list(APPEND FreeImage_LIBTIFF_SRCS 
      Source/LibTIFF4/tif_win32.c
    )
endif()
add_definitions(-DINCLUDE_LIB_TIFF4)
endif()

if(BUILD_ZLIB)
set(FreeImage_ZLIB_SRCS
Source/ZLib/adler32.c Source/ZLib/compress.c Source/ZLib/crc32.c Source/ZLib/deflate.c Source/ZLib/gzclose.c Source/ZLib/gzlib.c Source/ZLib/gzread.c Source/ZLib/gzwrite.c Source/ZLib/infback.c Source/ZLib/inffast.c Source/ZLib/inflate.c Source/ZLib/inftrees.c Source/ZLib/trees.c Source/ZLib/uncompr.c Source/ZLib/zutil.c
./Source/ZLib/crc32.h ./Source/ZLib/deflate.h ./Source/ZLib/gzguts.h ./Source/ZLib/inffast.h ./Source/ZLib/inffixed.h ./Source/ZLib/inflate.h ./Source/ZLib/inftrees.h ./Source/ZLib/trees.h ./Source/ZLib/zconf.h ./Source/ZLib/zlib.h ./Source/ZLib/zutil.h 
)
include_directories(Source/ZLib)
add_definitions(-DINCLUDE_LIB_ZLIB)
endif()

if(BUILD_JXR)
set(FreeImage_JXR_SRCS
    ./Source/LibJXR/image/decode/decode.c ./Source/LibJXR/image/decode/JXRTranscode.c ./Source/LibJXR/image/decode/postprocess.c ./Source/LibJXR/image/decode/segdec.c ./Source/LibJXR/image/decode/strInvTransform.c ./Source/LibJXR/image/ ./Source/FreeImage/PluginJXR.cpp
    ./Source/LibJXR/common/include/wmspecstring.h ./Source/LibJXR/common/include/wmspecstrings_adt.h ./Source/LibJXR/common/include/wmspecstrings_strict.h ./Source/LibJXR/common/include/wmspecstrings_undef.h ./Source/LibJXR/image/decode/decode.h ./Source/LibJXR/image/encode/encode.h ./Source/LibJXR/image/sys/ansi.h ./Source/LibJXR/image/sys/common.h ./Source/LibJXR/image/sys/perfTimer.h ./Source/LibJXR/image/sys/strcodec.h ./Source/LibJXR/image/sys/strTransform.h ./Source/LibJXR/image/sys/windowsmediaphoto.h ./Source/LibJXR/image/sys/xplatform_image.h ./Source/LibJXR/image/x86/x86.h ./Source/LibJXR/jxrgluelib/JXRGlue.h ./Source/LibJXR/jxrgluelib/JXRMeta.h
)    
include_directories(Source/LibJXR)
include_directories(Source/LibJXR/image/sys)
include_directories(Source/LibJXR/common/include)
include_directories(Source/LibJXR/jxrgluelib)
add_definitions(-DINCLUDE_LIB_JXR)
endif()

if(BUILD_WEBP)
set(FreeImage_WEBP_SRCS
Source/LibWebP/src/dec/alpha_dec.c Source/LibWebP/src/dec/buffer_dec.c Source/LibWebP/src/dec/frame_dec.c Source/LibWebP/src/dec/idec_dec.c Source/LibWebP/src/dec/io_dec.c Source/LibWebP/src/dec/quant_dec.c Source/LibWebP/src/dec/tree_dec.c Source/LibWebP/src/dec/vp8l_dec.c Source/LibWebP/src/dec/vp8_dec.c Source/LibWebP/src/dec/webp_dec.c Source/LibWebP/src/demux/anim_decode.c Source/LibWebP/src/demux/demux.c Source/LibWebP/src/dsp/alpha_processing.c Source/LibWebP/src/dsp/alpha_processing_mips_dsp_r2.c Source/LibWebP/src/dsp/alpha_processing_neon.c Source/LibWebP/src/dsp/alpha_processing_sse2.c Source/LibWebP/src/dsp/alpha_processing_sse41.c Source/LibWebP/src/dsp/cost.c Source/LibWebP/src/dsp/cost_mips32.c Source/LibWebP/src/dsp/cost_mips_dsp_r2.c Source/LibWebP/src/dsp/cost_neon.c Source/LibWebP/src/dsp/cost_sse2.c Source/LibWebP/src/dsp/cpu.c Source/LibWebP/src/dsp/dec.c Source/LibWebP/src/dsp/dec_clip_tables.c Source/LibWebP/src/dsp/dec_mips32.c Source/LibWebP/src/dsp/dec_mips_dsp_r2.c Source/LibWebP/src/dsp/dec_msa.c Source/LibWebP/src/dsp/dec_neon.c Source/LibWebP/src/dsp/dec_sse2.c Source/LibWebP/src/dsp/dec_sse41.c Source/LibWebP/src/dsp/enc.c Source/LibWebP/src/dsp/enc_avx2.c Source/LibWebP/src/dsp/enc_mips32.c Source/LibWebP/src/dsp/enc_mips_dsp_r2.c Source/LibWebP/src/dsp/enc_msa.c Source/LibWebP/src/dsp/enc_neon.c Source/LibWebP/src/dsp/enc_sse2.c Source/LibWebP/src/dsp/enc_sse41.c Source/LibWebP/src/dsp/filters.c Source/LibWebP/src/dsp/filters_mips_dsp_r2.c Source/LibWebP/src/dsp/filters_msa.c Source/LibWebP/src/dsp/filters_neon.c Source/LibWebP/src/dsp/filters_sse2.c Source/LibWebP/src/dsp/lossless.c Source/LibWebP/src/dsp/lossless_enc.c Source/LibWebP/src/dsp/lossless_enc_mips32.c Source/LibWebP/src/dsp/lossless_enc_mips_dsp_r2.c Source/LibWebP/src/dsp/lossless_enc_msa.c Source/LibWebP/src/dsp/lossless_enc_neon.c Source/LibWebP/src/dsp/lossless_enc_sse2.c Source/LibWebP/src/dsp/lossless_enc_sse41.c Source/LibWebP/src/dsp/lossless_mips_dsp_r2.c Source/LibWebP/src/dsp/lossless_msa.c Source/LibWebP/src/dsp/lossless_neon.c Source/LibWebP/src/dsp/lossless_sse2.c Source/LibWebP/src/dsp/lossless_sse41.c Source/LibWebP/src/dsp/rescaler.c Source/LibWebP/src/dsp/rescaler_mips32.c Source/LibWebP/src/dsp/rescaler_mips_dsp_r2.c Source/LibWebP/src/dsp/rescaler_msa.c Source/LibWebP/src/dsp/rescaler_neon.c Source/LibWebP/src/dsp/rescaler_sse2.c Source/LibWebP/src/dsp/ssim.c Source/LibWebP/src/dsp/ssim_sse2.c Source/LibWebP/src/dsp/upsampling.c Source/LibWebP/src/dsp/upsampling_mips_dsp_r2.c Source/LibWebP/src/dsp/upsampling_msa.c Source/LibWebP/src/dsp/upsampling_neon.c Source/LibWebP/src/dsp/upsampling_sse2.c Source/LibWebP/src/dsp/upsampling_sse41.c Source/LibWebP/src/dsp/yuv.c Source/LibWebP/src/dsp/yuv_mips32.c Source/LibWebP/src/dsp/yuv_mips_dsp_r2.c Source/LibWebP/src/dsp/yuv_neon.c Source/LibWebP/src/dsp/yuv_sse2.c Source/LibWebP/src/dsp/yuv_sse41.c Source/LibWebP/src/enc/alpha_enc.c Source/LibWebP/src/enc/analysis_enc.c Source/LibWebP/src/enc/backward_references_cost_enc.c Source/LibWebP/src/enc/backward_references_enc.c Source/LibWebP/src/enc/config_enc.c Source/LibWebP/src/enc/cost_enc.c Source/LibWebP/src/enc/filter_enc.c Source/LibWebP/src/enc/frame_enc.c Source/LibWebP/src/enc/histogram_enc.c Source/LibWebP/src/enc/iterator_enc.c Source/LibWebP/src/enc/near_lossless_enc.c Source/LibWebP/src/enc/picture_csp_enc.c Source/LibWebP/src/enc/picture_enc.c Source/LibWebP/src/enc/picture_psnr_enc.c Source/LibWebP/src/enc/picture_rescale_enc.c Source/LibWebP/src/enc/picture_tools_enc.c Source/LibWebP/src/enc/predictor_enc.c Source/LibWebP/src/enc/quant_enc.c Source/LibWebP/src/enc/syntax_enc.c Source/LibWebP/src/enc/token_enc.c Source/LibWebP/src/enc/tree_enc.c Source/LibWebP/src/enc/vp8l_enc.c Source/LibWebP/src/enc/webp_enc.c Source/LibWebP/src/mux/anim_encode.c Source/LibWebP/src/mux/muxedit.c Source/LibWebP/src/mux/muxinternal.c Source/LibWebP/src/mux/muxread.c Source/LibWebP/src/utils/bit_reader_utils.c Source/LibWebP/src/utils/bit_writer_utils.c Source/LibWebP/src/utils/color_cache_utils.c Source/LibWebP/src/utils/filters_utils.c Source/LibWebP/src/utils/huffman_encode_utils.c Source/LibWebP/src/utils/huffman_utils.c Source/LibWebP/src/utils/quant_levels_dec_utils.c Source/LibWebP/src/utils/quant_levels_utils.c Source/LibWebP/src/utils/random_utils.c Source/LibWebP/src/utils/rescaler_utils.c Source/LibWebP/src/utils/thread_utils.c Source/LibWebP/src/utils/utils.c
./Source/LibWebP/src/dec/alphai_dec.h ./Source/LibWebP/src/dec/common_dec.h ./Source/LibWebP/src/dec/vp8i_dec.h ./Source/LibWebP/src/dec/vp8li_dec.h ./Source/LibWebP/src/dec/vp8_dec.h ./Source/LibWebP/src/dec/webpi_dec.h ./Source/LibWebP/src/dsp/common_sse2.h ./Source/LibWebP/src/dsp/common_sse41.h ./Source/LibWebP/src/dsp/dsp.h ./Source/LibWebP/src/dsp/lossless.h ./Source/LibWebP/src/dsp/lossless_common.h ./Source/LibWebP/src/dsp/mips_macro.h ./Source/LibWebP/src/dsp/msa_macro.h ./Source/LibWebP/src/dsp/neon.h ./Source/LibWebP/src/dsp/quant.h ./Source/LibWebP/src/dsp/yuv.h ./Source/LibWebP/src/enc/backward_references_enc.h ./Source/LibWebP/src/enc/cost_enc.h ./Source/LibWebP/src/enc/histogram_enc.h ./Source/LibWebP/src/enc/vp8i_enc.h ./Source/LibWebP/src/enc/vp8li_enc.h ./Source/LibWebP/src/mux/animi.h ./Source/LibWebP/src/mux/muxi.h ./Source/LibWebP/src/utils/bit_reader_inl_utils.h ./Source/LibWebP/src/utils/bit_reader_utils.h ./Source/LibWebP/src/utils/bit_writer_utils.h ./Source/LibWebP/src/utils/color_cache_utils.h ./Source/LibWebP/src/utils/endian_inl_utils.h ./Source/LibWebP/src/utils/filters_utils.h ./Source/LibWebP/src/utils/huffman_encode_utils.h ./Source/LibWebP/src/utils/huffman_utils.h ./Source/LibWebP/src/utils/quant_levels_dec_utils.h ./Source/LibWebP/src/utils/quant_levels_utils.h ./Source/LibWebP/src/utils/random_utils.h ./Source/LibWebP/src/utils/rescaler_utils.h ./Source/LibWebP/src/utils/thread_utils.h ./Source/LibWebP/src/utils/utils.h ./Source/LibWebP/src/webp/decode.h ./Source/LibWebP/src/webp/demux.h ./Source/LibWebP/src/webp/encode.h ./Source/LibWebP/src/webp/format_constants.h ./Source/LibWebP/src/webp/mux.h ./Source/LibWebP/src/webp/mux_types.h ./Source/LibWebP/src/webp/types.h
)
include_directories(Source/LibWebP)
add_definitions(-DINCLUDE_LIB_WEBP)
endif()

if(BUILD_LIBRAWLITE)
set(FreeImage_LIBRAWLITE_SRCS
Source/LibRawLite/src/decoders/canon_600.cpp Source/LibRawLite/src/decoders/crx.cpp Source/LibRawLite/src/decoders/decoders_dcraw.cpp Source/LibRawLite/src/decoders/decoders_libraw.cpp Source/LibRawLite/src/decoders/decoders_libraw_dcrdefs.cpp Source/LibRawLite/src/decoders/dng.cpp Source/LibRawLite/src/decoders/fp_dng.cpp Source/LibRawLite/src/decoders/fuji_compressed.cpp Source/LibRawLite/src/decoders/generic.cpp Source/LibRawLite/src/decoders/kodak_decoders.cpp Source/LibRawLite/src/decoders/load_mfbacks.cpp Source/LibRawLite/src/decoders/smal.cpp Source/LibRawLite/src/decoders/unpack.cpp Source/LibRawLite/src/decoders/unpack_thumb.cpp Source/LibRawLite/src/demosaic/aahd_demosaic.cpp Source/LibRawLite/src/demosaic/ahd_demosaic.cpp Source/LibRawLite/src/demosaic/dcb_demosaic.cpp Source/LibRawLite/src/demosaic/dht_demosaic.cpp Source/LibRawLite/src/demosaic/misc_demosaic.cpp Source/LibRawLite/src/demosaic/xtrans_demosaic.cpp Source/LibRawLite/src/integration/dngsdk_glue.cpp Source/LibRawLite/src/integration/rawspeed_glue.cpp Source/LibRawLite/src/libraw_datastream.cpp Source/LibRawLite/src/metadata/adobepano.cpp Source/LibRawLite/src/metadata/canon.cpp Source/LibRawLite/src/metadata/ciff.cpp Source/LibRawLite/src/metadata/cr3_parser.cpp Source/LibRawLite/src/metadata/epson.cpp Source/LibRawLite/src/metadata/exif_gps.cpp Source/LibRawLite/src/metadata/fuji.cpp Source/LibRawLite/src/metadata/hasselblad_model.cpp Source/LibRawLite/src/metadata/identify.cpp Source/LibRawLite/src/metadata/identify_tools.cpp Source/LibRawLite/src/metadata/kodak.cpp Source/LibRawLite/src/metadata/leica.cpp Source/LibRawLite/src/metadata/makernotes.cpp Source/LibRawLite/src/metadata/mediumformat.cpp Source/LibRawLite/src/metadata/minolta.cpp Source/LibRawLite/src/metadata/misc_parsers.cpp Source/LibRawLite/src/metadata/nikon.cpp Source/LibRawLite/src/metadata/normalize_model.cpp Source/LibRawLite/src/metadata/olympus.cpp Source/LibRawLite/src/metadata/p1.cpp Source/LibRawLite/src/metadata/pentax.cpp Source/LibRawLite/src/metadata/samsung.cpp Source/LibRawLite/src/metadata/sony.cpp Source/LibRawLite/src/metadata/tiff.cpp Source/LibRawLite/src/postprocessing/aspect_ratio.cpp Source/LibRawLite/src/postprocessing/dcraw_process.cpp Source/LibRawLite/src/postprocessing/mem_image.cpp Source/LibRawLite/src/postprocessing/postprocessing_aux.cpp Source/LibRawLite/src/postprocessing/postprocessing_utils.cpp Source/LibRawLite/src/postprocessing/postprocessing_utils_dcrdefs.cpp Source/LibRawLite/src/preprocessing/ext_preprocess.cpp Source/LibRawLite/src/preprocessing/raw2image.cpp Source/LibRawLite/src/preprocessing/subtract_black.cpp Source/LibRawLite/src/tables/cameralist.cpp Source/LibRawLite/src/tables/colorconst.cpp Source/LibRawLite/src/tables/colordata.cpp Source/LibRawLite/src/tables/wblists.cpp Source/LibRawLite/src/utils/curves.cpp Source/LibRawLite/src/utils/decoder_info.cpp Source/LibRawLite/src/utils/init_close_utils.cpp Source/LibRawLite/src/utils/open.cpp Source/LibRawLite/src/utils/phaseone_processing.cpp Source/LibRawLite/src/utils/read_utils.cpp Source/LibRawLite/src/utils/thumb_utils.cpp Source/LibRawLite/src/utils/utils_dcraw.cpp Source/LibRawLite/src/utils/utils_libraw.cpp Source/LibRawLite/src/write/file_write.cpp Source/LibRawLite/src/x3f/x3f_parse_process.cpp Source/LibRawLite/src/x3f/x3f_utils_patched.cpp
./Source/LibRawLite/internal/dcraw_defs.h ./Source/LibRawLite/internal/dcraw_fileio_defs.h ./Source/LibRawLite/internal/defines.h ./Source/LibRawLite/internal/dmp_include.h ./Source/LibRawLite/internal/libraw_cameraids.h ./Source/LibRawLite/internal/libraw_cxx_defs.h ./Source/LibRawLite/internal/libraw_internal_funcs.h ./Source/LibRawLite/internal/var_defines.h ./Source/LibRawLite/internal/x3f_tools.h ./Source/LibRawLite/libraw/libraw.h ./Source/LibRawLite/libraw/libraw_alloc.h ./Source/LibRawLite/libraw/libraw_const.h ./Source/LibRawLite/libraw/libraw_datastream.h ./Source/LibRawLite/libraw/libraw_internal.h ./Source/LibRawLite/libraw/libraw_types.h ./Source/LibRawLite/libraw/libraw_version.h
)
include_directories(Source/LibRawLite)
include_directories(Source/LibRawLite/dcraw)
include_directories(Source/LibRawLite/internal)
include_directories(Source/LibRawLite/libraw)
include_directories(Source/LibRawLite/src)
add_definitions(-DINCLUDE_LIB_RAW)
endif()



set(FreeImage_OPENEXR_HALF_SRCS
Source/OpenEXR/Half/half.cpp Source/OpenEXR/Half/eLut.cpp Source/OpenEXR/Half/toFloat.cpp
./Source/OpenEXR/Half/eLut.h ./Source/OpenEXR/Half/half.h ./Source/OpenEXR/Half/halfExport.h ./Source/OpenEXR/Half/halfFunction.h ./Source/OpenEXR/Half/halfLimits.h ./Source/OpenEXR/Half/toFloat.h
)
include_directories(Source/OpenEXR/Half)


if(BUILD_OPENEXR)
set(FreeImage_OPENEXR_SRCS
Source/OpenEXR/IexMath/IexMathFpu.cpp Source/OpenEXR/IlmImf/b44ExpLogTable.cpp Source/OpenEXR/IlmImf/ImfAcesFile.cpp Source/OpenEXR/IlmImf/ImfAttribute.cpp Source/OpenEXR/IlmImf/ImfB44Compressor.cpp Source/OpenEXR/IlmImf/ImfBoxAttribute.cpp Source/OpenEXR/IlmImf/ImfChannelList.cpp Source/OpenEXR/IlmImf/ImfChannelListAttribute.cpp Source/OpenEXR/IlmImf/ImfChromaticities.cpp Source/OpenEXR/IlmImf/ImfChromaticitiesAttribute.cpp Source/OpenEXR/IlmImf/ImfCompositeDeepScanLine.cpp Source/OpenEXR/IlmImf/ImfCompressionAttribute.cpp Source/OpenEXR/IlmImf/ImfCompressor.cpp Source/OpenEXR/IlmImf/ImfConvert.cpp Source/OpenEXR/IlmImf/ImfCRgbaFile.cpp Source/OpenEXR/IlmImf/ImfDeepCompositing.cpp Source/OpenEXR/IlmImf/ImfDeepFrameBuffer.cpp Source/OpenEXR/IlmImf/ImfDeepImageStateAttribute.cpp Source/OpenEXR/IlmImf/ImfDeepScanLineInputFile.cpp Source/OpenEXR/IlmImf/ImfDeepScanLineInputPart.cpp Source/OpenEXR/IlmImf/ImfDeepScanLineOutputFile.cpp Source/OpenEXR/IlmImf/ImfDeepScanLineOutputPart.cpp Source/OpenEXR/IlmImf/ImfDeepTiledInputFile.cpp Source/OpenEXR/IlmImf/ImfDeepTiledInputPart.cpp Source/OpenEXR/IlmImf/ImfDeepTiledOutputFile.cpp Source/OpenEXR/IlmImf/ImfDeepTiledOutputPart.cpp Source/OpenEXR/IlmImf/ImfDoubleAttribute.cpp Source/OpenEXR/IlmImf/ImfDwaCompressor.cpp Source/OpenEXR/IlmImf/ImfEnvmap.cpp Source/OpenEXR/IlmImf/ImfEnvmapAttribute.cpp Source/OpenEXR/IlmImf/ImfFastHuf.cpp Source/OpenEXR/IlmImf/ImfFloatAttribute.cpp Source/OpenEXR/IlmImf/ImfFloatVectorAttribute.cpp Source/OpenEXR/IlmImf/ImfFrameBuffer.cpp Source/OpenEXR/IlmImf/ImfFramesPerSecond.cpp Source/OpenEXR/IlmImf/ImfGenericInputFile.cpp Source/OpenEXR/IlmImf/ImfGenericOutputFile.cpp Source/OpenEXR/IlmImf/ImfHeader.cpp Source/OpenEXR/IlmImf/ImfHuf.cpp Source/OpenEXR/IlmImf/ImfInputFile.cpp Source/OpenEXR/IlmImf/ImfInputPart.cpp Source/OpenEXR/IlmImf/ImfInputPartData.cpp Source/OpenEXR/IlmImf/ImfIntAttribute.cpp Source/OpenEXR/IlmImf/ImfIO.cpp Source/OpenEXR/IlmImf/ImfKeyCode.cpp Source/OpenEXR/IlmImf/ImfKeyCodeAttribute.cpp Source/OpenEXR/IlmImf/ImfLineOrderAttribute.cpp Source/OpenEXR/IlmImf/ImfLut.cpp Source/OpenEXR/IlmImf/ImfMatrixAttribute.cpp Source/OpenEXR/IlmImf/ImfMisc.cpp Source/OpenEXR/IlmImf/ImfMultiPartInputFile.cpp Source/OpenEXR/IlmImf/ImfMultiPartOutputFile.cpp Source/OpenEXR/IlmImf/ImfMultiView.cpp Source/OpenEXR/IlmImf/ImfOpaqueAttribute.cpp Source/OpenEXR/IlmImf/ImfOutputFile.cpp Source/OpenEXR/IlmImf/ImfOutputPart.cpp Source/OpenEXR/IlmImf/ImfOutputPartData.cpp Source/OpenEXR/IlmImf/ImfPartType.cpp Source/OpenEXR/IlmImf/ImfPizCompressor.cpp Source/OpenEXR/IlmImf/ImfPreviewImage.cpp Source/OpenEXR/IlmImf/ImfPreviewImageAttribute.cpp Source/OpenEXR/IlmImf/ImfPxr24Compressor.cpp Source/OpenEXR/IlmImf/ImfRational.cpp Source/OpenEXR/IlmImf/ImfRationalAttribute.cpp Source/OpenEXR/IlmImf/ImfRgbaFile.cpp Source/OpenEXR/IlmImf/ImfRgbaYca.cpp Source/OpenEXR/IlmImf/ImfRle.cpp Source/OpenEXR/IlmImf/ImfRleCompressor.cpp Source/OpenEXR/IlmImf/ImfScanLineInputFile.cpp Source/OpenEXR/IlmImf/ImfStandardAttributes.cpp Source/OpenEXR/IlmImf/ImfStdIO.cpp Source/OpenEXR/IlmImf/ImfStringAttribute.cpp Source/OpenEXR/IlmImf/ImfStringVectorAttribute.cpp Source/OpenEXR/IlmImf/ImfSystemSpecific.cpp Source/OpenEXR/IlmImf/ImfTestFile.cpp Source/OpenEXR/IlmImf/ImfThreading.cpp Source/OpenEXR/IlmImf/ImfTileDescriptionAttribute.cpp Source/OpenEXR/IlmImf/ImfTiledInputFile.cpp Source/OpenEXR/IlmImf/ImfTiledInputPart.cpp Source/OpenEXR/IlmImf/ImfTiledMisc.cpp Source/OpenEXR/IlmImf/ImfTiledOutputFile.cpp Source/OpenEXR/IlmImf/ImfTiledOutputPart.cpp Source/OpenEXR/IlmImf/ImfTiledRgbaFile.cpp Source/OpenEXR/IlmImf/ImfTileOffsets.cpp Source/OpenEXR/IlmImf/ImfTimeCode.cpp Source/OpenEXR/IlmImf/ImfTimeCodeAttribute.cpp Source/OpenEXR/IlmImf/ImfVecAttribute.cpp Source/OpenEXR/IlmImf/ImfVersion.cpp Source/OpenEXR/IlmImf/ImfWav.cpp Source/OpenEXR/IlmImf/ImfZip.cpp Source/OpenEXR/IlmImf/ImfZipCompressor.cpp Source/OpenEXR/Imath/ImathBox.cpp Source/OpenEXR/Imath/ImathColorAlgo.cpp Source/OpenEXR/Imath/ImathFun.cpp Source/OpenEXR/Imath/ImathMatrixAlgo.cpp Source/OpenEXR/Imath/ImathRandom.cpp Source/OpenEXR/Imath/ImathShear.cpp Source/OpenEXR/Imath/ImathVec.cpp Source/OpenEXR/Iex/IexBaseExc.cpp Source/OpenEXR/Iex/IexThrowErrnoExc.cpp  Source/OpenEXR/IlmThread/IlmThread.cpp Source/OpenEXR/IlmThread/IlmThreadMutex.cpp Source/OpenEXR/IlmThread/IlmThreadPool.cpp Source/OpenEXR/IlmThread/IlmThreadSemaphore.cpp Source/OpenEXR/IexMath/IexMathFloatExc.cpp
 ./Source/OpenEXR/Iex/Iex.h ./Source/OpenEXR/Iex/IexBaseExc.h ./Source/OpenEXR/Iex/IexErrnoExc.h ./Source/OpenEXR/Iex/IexExport.h ./Source/OpenEXR/Iex/IexForward.h ./Source/OpenEXR/Iex/IexMacros.h ./Source/OpenEXR/Iex/IexMathExc.h ./Source/OpenEXR/Iex/IexNamespace.h ./Source/OpenEXR/Iex/IexThrowErrnoExc.h ./Source/OpenEXR/IexMath/IexMathFloatExc.h ./Source/OpenEXR/IexMath/IexMathFpu.h ./Source/OpenEXR/IexMath/IexMathIeeeExc.h ./Source/OpenEXR/IlmBaseConfig.h ./Source/OpenEXR/IlmImf/b44ExpLogTable.h ./Source/OpenEXR/IlmImf/dwaLookups.h ./Source/OpenEXR/IlmImf/ImfAcesFile.h ./Source/OpenEXR/IlmImf/ImfArray.h ./Source/OpenEXR/IlmImf/ImfAttribute.h ./Source/OpenEXR/IlmImf/ImfAutoArray.h ./Source/OpenEXR/IlmImf/ImfB44Compressor.h ./Source/OpenEXR/IlmImf/ImfBoxAttribute.h ./Source/OpenEXR/IlmImf/ImfChannelList.h ./Source/OpenEXR/IlmImf/ImfChannelListAttribute.h ./Source/OpenEXR/IlmImf/ImfCheckedArithmetic.h ./Source/OpenEXR/IlmImf/ImfChromaticities.h ./Source/OpenEXR/IlmImf/ImfChromaticitiesAttribute.h ./Source/OpenEXR/IlmImf/ImfCompositeDeepScanLine.h ./Source/OpenEXR/IlmImf/ImfCompression.h ./Source/OpenEXR/IlmImf/ImfCompressionAttribute.h ./Source/OpenEXR/IlmImf/ImfCompressor.h ./Source/OpenEXR/IlmImf/ImfConvert.h ./Source/OpenEXR/IlmImf/ImfCRgbaFile.h ./Source/OpenEXR/IlmImf/ImfDeepCompositing.h ./Source/OpenEXR/IlmImf/ImfDeepFrameBuffer.h ./Source/OpenEXR/IlmImf/ImfDeepImageState.h ./Source/OpenEXR/IlmImf/ImfDeepImageStateAttribute.h ./Source/OpenEXR/IlmImf/ImfDeepScanLineInputFile.h ./Source/OpenEXR/IlmImf/ImfDeepScanLineInputPart.h ./Source/OpenEXR/IlmImf/ImfDeepScanLineOutputFile.h ./Source/OpenEXR/IlmImf/ImfDeepScanLineOutputPart.h ./Source/OpenEXR/IlmImf/ImfDeepTiledInputFile.h ./Source/OpenEXR/IlmImf/ImfDeepTiledInputPart.h ./Source/OpenEXR/IlmImf/ImfDeepTiledOutputFile.h ./Source/OpenEXR/IlmImf/ImfDeepTiledOutputPart.h ./Source/OpenEXR/IlmImf/ImfDoubleAttribute.h ./Source/OpenEXR/IlmImf/ImfDwaCompressor.h ./Source/OpenEXR/IlmImf/ImfDwaCompressorSimd.h ./Source/OpenEXR/IlmImf/ImfEnvmap.h ./Source/OpenEXR/IlmImf/ImfEnvmapAttribute.h ./Source/OpenEXR/IlmImf/ImfExport.h ./Source/OpenEXR/IlmImf/ImfFastHuf.h ./Source/OpenEXR/IlmImf/ImfFloatAttribute.h ./Source/OpenEXR/IlmImf/ImfFloatVectorAttribute.h ./Source/OpenEXR/IlmImf/ImfForward.h ./Source/OpenEXR/IlmImf/ImfFrameBuffer.h ./Source/OpenEXR/IlmImf/ImfFramesPerSecond.h ./Source/OpenEXR/IlmImf/ImfGenericInputFile.h ./Source/OpenEXR/IlmImf/ImfGenericOutputFile.h ./Source/OpenEXR/IlmImf/ImfHeader.h ./Source/OpenEXR/IlmImf/ImfHuf.h ./Source/OpenEXR/IlmImf/ImfInputFile.h ./Source/OpenEXR/IlmImf/ImfInputPart.h ./Source/OpenEXR/IlmImf/ImfInputPartData.h ./Source/OpenEXR/IlmImf/ImfInputStreamMutex.h ./Source/OpenEXR/IlmImf/ImfInt64.h ./Source/OpenEXR/IlmImf/ImfIntAttribute.h ./Source/OpenEXR/IlmImf/ImfIO.h ./Source/OpenEXR/IlmImf/ImfKeyCode.h ./Source/OpenEXR/IlmImf/ImfKeyCodeAttribute.h ./Source/OpenEXR/IlmImf/ImfLineOrder.h ./Source/OpenEXR/IlmImf/ImfLineOrderAttribute.h ./Source/OpenEXR/IlmImf/ImfLut.h ./Source/OpenEXR/IlmImf/ImfMatrixAttribute.h ./Source/OpenEXR/IlmImf/ImfMisc.h ./Source/OpenEXR/IlmImf/ImfMultiPartInputFile.h ./Source/OpenEXR/IlmImf/ImfMultiPartOutputFile.h ./Source/OpenEXR/IlmImf/ImfMultiView.h ./Source/OpenEXR/IlmImf/ImfName.h ./Source/OpenEXR/IlmImf/ImfNamespace.h ./Source/OpenEXR/IlmImf/ImfOpaqueAttribute.h ./Source/OpenEXR/IlmImf/ImfOptimizedPixelReading.h ./Source/OpenEXR/IlmImf/ImfOutputFile.h ./Source/OpenEXR/IlmImf/ImfOutputPart.h ./Source/OpenEXR/IlmImf/ImfOutputPartData.h ./Source/OpenEXR/IlmImf/ImfOutputStreamMutex.h ./Source/OpenEXR/IlmImf/ImfPartHelper.h ./Source/OpenEXR/IlmImf/ImfPartType.h ./Source/OpenEXR/IlmImf/ImfPixelType.h ./Source/OpenEXR/IlmImf/ImfPizCompressor.h ./Source/OpenEXR/IlmImf/ImfPreviewImage.h ./Source/OpenEXR/IlmImf/ImfPreviewImageAttribute.h ./Source/OpenEXR/IlmImf/ImfPxr24Compressor.h ./Source/OpenEXR/IlmImf/ImfRational.h ./Source/OpenEXR/IlmImf/ImfRationalAttribute.h ./Source/OpenEXR/IlmImf/ImfRgba.h ./Source/OpenEXR/IlmImf/ImfRgbaFile.h ./Source/OpenEXR/IlmImf/ImfRgbaYca.h ./Source/OpenEXR/IlmImf/ImfRle.h ./Source/OpenEXR/IlmImf/ImfRleCompressor.h ./Source/OpenEXR/IlmImf/ImfScanLineInputFile.h ./Source/OpenEXR/IlmImf/ImfSimd.h ./Source/OpenEXR/IlmImf/ImfStandardAttributes.h ./Source/OpenEXR/IlmImf/ImfStdIO.h ./Source/OpenEXR/IlmImf/ImfStringAttribute.h ./Source/OpenEXR/IlmImf/ImfStringVectorAttribute.h ./Source/OpenEXR/IlmImf/ImfSystemSpecific.h ./Source/OpenEXR/IlmImf/ImfTestFile.h ./Source/OpenEXR/IlmImf/ImfThreading.h ./Source/OpenEXR/IlmImf/ImfTileDescription.h ./Source/OpenEXR/IlmImf/ImfTileDescriptionAttribute.h ./Source/OpenEXR/IlmImf/ImfTiledInputFile.h ./Source/OpenEXR/IlmImf/ImfTiledInputPart.h ./Source/OpenEXR/IlmImf/ImfTiledMisc.h ./Source/OpenEXR/IlmImf/ImfTiledOutputFile.h ./Source/OpenEXR/IlmImf/ImfTiledOutputPart.h ./Source/OpenEXR/IlmImf/ImfTiledRgbaFile.h ./Source/OpenEXR/IlmImf/ImfTileOffsets.h ./Source/OpenEXR/IlmImf/ImfTimeCode.h ./Source/OpenEXR/IlmImf/ImfTimeCodeAttribute.h ./Source/OpenEXR/IlmImf/ImfVecAttribute.h ./Source/OpenEXR/IlmImf/ImfVersion.h ./Source/OpenEXR/IlmImf/ImfWav.h ./Source/OpenEXR/IlmImf/ImfXdr.h ./Source/OpenEXR/IlmImf/ImfZip.h ./Source/OpenEXR/IlmImf/ImfZipCompressor.h ./Source/OpenEXR/IlmThread/IlmThread.h ./Source/OpenEXR/IlmThread/IlmThreadExport.h ./Source/OpenEXR/IlmThread/IlmThreadForward.h ./Source/OpenEXR/IlmThread/IlmThreadMutex.h ./Source/OpenEXR/IlmThread/IlmThreadNamespace.h ./Source/OpenEXR/IlmThread/IlmThreadPool.h ./Source/OpenEXR/IlmThread/IlmThreadSemaphore.h ./Source/OpenEXR/Imath/ImathBox.h ./Source/OpenEXR/Imath/ImathBoxAlgo.h ./Source/OpenEXR/Imath/ImathColor.h ./Source/OpenEXR/Imath/ImathColorAlgo.h ./Source/OpenEXR/Imath/ImathEuler.h ./Source/OpenEXR/Imath/ImathExc.h ./Source/OpenEXR/Imath/ImathExport.h ./Source/OpenEXR/Imath/ImathForward.h ./Source/OpenEXR/Imath/ImathFrame.h ./Source/OpenEXR/Imath/ImathFrustum.h ./Source/OpenEXR/Imath/ImathFrustumTest.h ./Source/OpenEXR/Imath/ImathFun.h ./Source/OpenEXR/Imath/ImathGL.h ./Source/OpenEXR/Imath/ImathGLU.h ./Source/OpenEXR/Imath/ImathHalfLimits.h ./Source/OpenEXR/Imath/ImathInt64.h ./Source/OpenEXR/Imath/ImathInterval.h ./Source/OpenEXR/Imath/ImathLimits.h ./Source/OpenEXR/Imath/ImathLine.h ./Source/OpenEXR/Imath/ImathLineAlgo.h ./Source/OpenEXR/Imath/ImathMath.h ./Source/OpenEXR/Imath/ImathMatrix.h ./Source/OpenEXR/Imath/ImathMatrixAlgo.h ./Source/OpenEXR/Imath/ImathNamespace.h ./Source/OpenEXR/Imath/ImathPlane.h ./Source/OpenEXR/Imath/ImathPlatform.h ./Source/OpenEXR/Imath/ImathQuat.h ./Source/OpenEXR/Imath/ImathRandom.h ./Source/OpenEXR/Imath/ImathRoots.h ./Source/OpenEXR/Imath/ImathShear.h ./Source/OpenEXR/Imath/ImathSphere.h ./Source/OpenEXR/Imath/ImathVec.h ./Source/OpenEXR/Imath/ImathVecAlgo.h ./Source/OpenEXR/OpenEXRConfig.h
)
include_directories(Source/OpenEXR)
include_directories(Source/OpenEXR/Half)
include_directories(Source/OpenEXR/Iex)
include_directories(Source/OpenEXR/IlmImf)
include_directories(Source/OpenEXR/IlmThread)
include_directories(Source/OpenEXR/IexMath)
include_directories(Source/OpenEXR/Imath)
add_definitions(-DINCLUDE_LIB_OPENEXR)
endif()



# need include directories for FreeImage and all the sub libs
include_directories(Source)
include_directories(Source/Metadata)
include_directories(Source/FreeImageToolkit)
include_directories(Source/LibJPEG)
include_directories(Source/LibPNG)
include_directories(Source/LibTIFF4)
include_directories(Source/LibOpenJPEG)




add_definitions(-DOPJ_STATIC -DNO_WINDOWS -DNDEBUG -DNO_LCMS -D__ANSI__ -DDISABLE_PERF_MEASUREMENT -DFREEIMAGE_LIB -DNO_LCMS)

add_library(FreeImage STATIC 
    ${FreeImage_SOURCES}  
    ${FreeImage_ZLIB_SRCS}
    ${FreeImage_JXR_SRCS}
    ${FreeImage_WEBP_SRCS}
    ${FreeImage_OPENEXR_SRCS}
    ${FreeImage_LIBRAWLITE_SRCS}
    ${FreeImage_LIBTIFF_SRCS}
    ${FreeImage_OPENEXR_HALF_SRCS}
)
#install_dep(FreeImage include Source/FreeImage.h)

if(EMSCRIPTEN)
    set(EMSCRIPTEN_CORE_SOURCES
        ${FreeImage_SOURCES}  
    	${FreeImage_ZLIB_SRCS}
    	${FreeImage_JXR_SRCS}
    	${FreeImage_WEBP_SRCS}
    	${FreeImage_OPENEXR_SRCS}
    	${FreeImage_LIBRAWLITE_SRCS}
    	${FreeImage_LIBTIFF_SRCS}
    	${FreeImage_OPENEXR_HALF_SRCS}
    )
    add_executable(FreeImage_wasm
         ${EMSCRIPTEN_CORE_SOURCES}
    )
endif()

if (APPLE)
 set_target_properties(FreeImage PROPERTIES XCODE_ATTRIBUTE_ONLY_ACTIVE_ARCH "NO")

 if(BUILD_PLATFORM_APPLE_IOS)
  set_target_properties(FreeImage PROPERTIES XCODE_ATTRIBUTE_GCC_THUMB_SUPPORT "NO")
 endif()
endif()

set(FreeImage_INCLUDE_DIR "${FreeImage_SOURCE_DIR}/Source" CACHE PATH "" FORCE)
set(FreeImage_LIBRARY_DBG FreeImage CACHE STRING "" FORCE)
set(FreeImage_LIBRARY_REL FreeImage CACHE STRING "" FORCE)
mark_as_advanced(FreeImage_INCLUDE_DIR FreeImage_LIBRARY_DBG FreeImage_LIBRARY_REL)

INSTALL (
    DIRECTORY ${CMAKE_SOURCE_DIR}/Source/
    DESTINATION include
    FILES_MATCHING PATTERN "*.h*")
