#Sycon V2.0 Round Function Area Analysis Script clean_all
#set lib uk65lscllmvbbh_120c25_tc
set lib fse0a_d_generic_core_ff1p1vm40c
set design round
set WDIR "C:/Users/dhima/OneDrive/Documents/MEGA/hardware/syconv2hw/"
set PERMPATH "C:/Users/dhima/OneDrive/Documents/MEGA/hardware/syconv2hw/source/perm" 
set perm [list mLayerOpt mux rLayer sbox sLayer pLayer1 ipLayer1 round]

load_library $lib set_working_dir $WDIR




foreach file $perm {
read -technology "$lib" [list $PERMPATH/$perm_sheet_final.v] 
}


pre_optimize -common_logic -unused_logic -boundary -xor_comparator_optimize
pre_optimize -extract
pd


optimize .work.$design.INTERFACE -target "$lib" -macro -area -effort quick -hierarchy auto 
optimize_timing .work.$design.INTERFACE


report_area $design\_asic_area_report.txt -cell_usage -hierarchy -all_leafs 
report_delay -num_paths 1 -critical_paths -clock_frequency
set novendor_constraint_file FALSE
auto_write -downto PRIMITIVES out_$design.v
