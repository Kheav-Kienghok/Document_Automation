# SheerID 验证配置文件

# SheerID API 配置
PROGRAM_ID = "681d40e03e7a8077098cb1b6"
SHEERID_BASE_URL = "https://services.sheerid.com"
MY_SHEERID_URL = "https://my.sheerid.com"


# 文件大小限制
MAX_FILE_SIZE = 1 * 1024 * 1024  # 1MB

# 学校配置 - Pennsylvania State University 多校区
SCHOOLS = {
    "10207763": {
        "id": 10207763,
        "idExtended": "10207763",
        "name": "Saint Benet Biscop Catholic Academy (Bedlington)",
    },
}

# 默认学校
DEFAULT_SCHOOL_ID = '10207763'
