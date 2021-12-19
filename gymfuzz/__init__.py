import os

from gym.envs.registration import register


def afl_forkserver_path():
    package_directory = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(
        package_directory, 'mods/afl-2.52b-mod/afl-2.52b/afl-forkserver',
    )


def simple_bits_target_path():
    package_directory = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(
        package_directory, 'mods/simple_bits-mod/simple_bits_afl',
    )


register(
    id='FuzzSimpleBits-v0',
    entry_point='gymfuzz.envs:FuzzSimpleBitsEnv',
)


def simple_loop_target_path():
    package_directory = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(
        package_directory, 'mods/simple_loop-mod/simple_loop_afl',
    )


register(
    id='FuzzSimpleLoop-v0',
    entry_point='gymfuzz.envs:FuzzSimpleLoopEnv',
)


def checksum_k_n_target_path():
    package_directory = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(
        package_directory, 'mods/checksum_k_n-mod/checksum_k_n_afl',
    )


register(
    id='FuzzChecksum_2_2-v0',
    entry_point='gymfuzz.envs:FuzzChecksum_2_2Env',
)
register(
    id='FuzzChecksum_4_2-v0',
    entry_point='gymfuzz.envs:FuzzChecksum_4_2Env',
)
register(
    id='FuzzChecksum_8_2-v0',
    entry_point='gymfuzz.envs:FuzzChecksum_8_2Env',
)
register(
    id='FuzzChecksum_2_4-v0',
    entry_point='gymfuzz.envs:FuzzChecksum_2_4Env',
)
register(
    id='FuzzChecksum_4_4-v0',
    entry_point='gymfuzz.envs:FuzzChecksum_4_4Env',
)
register(
    id='FuzzChecksum_8_4-v0',
    entry_point='gymfuzz.envs:FuzzChecksum_8_4Env',
)
register(
    id='FuzzChecksum_2_8-v0',
    entry_point='gymfuzz.envs:FuzzChecksum_2_8Env',
)
register(
    id='FuzzChecksum_8_8-v0',
    entry_point='gymfuzz.envs:FuzzChecksum_8_8Env',
)

# add
def libxml_target_path():
    package_directory = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(
        package_directory, 'mods/libxml-2.9.2-mod/libxml_afl',
    )

register(
    id='FuzzLibXML-v0',
    entry_point='gymfuzz.envs:FuzzLibXMLEnv',
)


def libpng12_target_path():
    package_directory = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(
        package_directory, 'mods/libpng-1.2.56-mod/libpng_1.2.56_afl',
    )


def libpng16_target_path():
    package_directory = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(
        package_directory, 'mods/libpng-1.6.34-mod/libpng_simple_fopen_afl',
    )


register(
    id='FuzzLibPNG12-v0',
    entry_point='gymfuzz.envs:FuzzLibPNG12Env',
)

register(
    id='FuzzLibPNG16-v0',
    entry_point='gymfuzz.envs:FuzzLibPNG16Env',
)


def sqlite_target_path():
    package_directory = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(
        package_directory, 'mods/sqlite3-mod/sqlite3_afl',
    )

register(
    id='FuzzSqlite-v0',
    entry_point='gymfuzz.envs:FuzzSqliteEnv',
)


def libjpeg_target_path():
    package_directory = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(
        package_directory, 'mods/libjpeg_turbo-mod/libjpeg_turbo_afl',
    )

register(
    id='FuzzLibJPEG-v0',
    entry_point='gymfuzz.envs:FuzzLibJPEGEnv',
)