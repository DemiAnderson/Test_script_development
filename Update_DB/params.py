DATA = {
    "sales": {
        "FOLDER_PATH_IN": 'C:\\Users\\dmandree\\Downloads\\TL_new',
        "FOLDER_PATH_OUT": 'C:\\Users\\dmandree\\Downloads\\TL_arch',
        "SHEET": 'TurnoverList',
        "COL_NAMES": ['Day', 'Store', 'Company', 'Open', 'Amount', 'Curr', 'Pcs', 'Rcp', 'People', 'Hours', 'Work', 'Comp:', 'Open_1', 'Amount_1', 'Curr_1', 'Pcs_1', 'Rcp_1', 'People_1', 'Hours_1', 'Work_1'],
        "COMPANIES": ['Guess Kazakhstan', 'Guess CIS'],
        "SKIP": 0,
        "IF_EXISTS": 'append'
    },
    "ms_sales": {
        "FOLDER_PATH_IN": 'C:\\Users\\dmandree\\Downloads\\RTL_new',
        "FOLDER_PATH_OUT": 'C:\\Users\\dmandree\\Downloads\\RTL_arch',
        "SHEET": 'RTL50000_by_season_by_store old',
        "COL_NAMES": ['Company', 'Country', 'Day', 'Mfg Season', 'Line Code', 'Gender', 'Dept Group', 'Dept', 'Sub Dept', 'Class', 'Class_1', 'Style', 'Style_1', 'Chain', 'Store', 'Store_1', 'Metrics', 'Ttl Sls Qty', 'TTL Curr Rtl Price €', 'Discount €', 'Ttl Sls €', 'Ttl Cost LC', 'Ttl Sls Trasp Cost LC', 'Ttl Cost €', 'Ttl Sls LC', 'Ttl Sls Trasp Cost €'],
        "COMPANIES": ['RU', 'KZ'],
        "SKIP": 3,
        "IF_EXISTS": 'append'
    },
    "ms_stock": {
        "FOLDER_PATH_IN": 'C:\\Users\\dmandree\\Downloads\\FNC_new',
        "FOLDER_PATH_OUT": 'C:\\Users\\dmandree\\Downloads\\FNC_arch',
        "SHEET": 'FNC03-50001-Margin_stock all st',
        "COL_NAMES": ['Company', 'Day', 'Store', 'Store_1', 'Mfg Season', 'Line Code', 'Line_Code_1', 'Style', 'Style_1', 'Sub_Dept', 'Sub_Dept_1', 'Metrics', 'TTL EOH Ttl Qty', 'TTL Loading Cost €', 'TTL Loading Cost LC', 'TTL Trasp Cost €', 'Cost €'],
        "COMPANIES": ['RU', 'KZ'],
        "SKIP": 2,
        "IF_EXISTS": 'replace'
    }
}

RAW_DATA_PATH = '\\\\rumo1w6vfs001.guess.eu\\Data\\Finance\\Andreev\\MS Data'

# File for Dict path
DICT_PATH = 'C:\\Users\\dmandree\\OneDrive - Guess Inc\\D Project\\Dict\\Mapping.xlsx'

# List of pages that we transform into dataframes
LIST_OF_SHEETS = [
    "Stores", 
    "Dist_managers", 
    "VM", 
    "Fin_Calendar_old", 
    "Fin_Calendar_new", 
    "Template", 
    "Start_date", 
    "Comp_flags", 
    "Comp_flags_alter", 
    "Targets"
    ]

MAT_VIEWS = ["public.ms_basic_mv", "public.ms_basic_mini"]
