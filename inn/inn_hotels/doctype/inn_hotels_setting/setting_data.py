def get_account():
	accounts = [
		{
			"account_name": "Asset",
			"parent_number": "",
			"account_number": "1000.000",
			"is_group": "1",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Asset"
		},
		{
			"account_name": "Current Asset",
			"parent_number": "1000.000",
			"account_number": "1100.000",
			"is_group": "1",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Asset"
		},
		{
			"account_name": "Cash",
			"parent_number": "1100.000",
			"account_number": "1110.000",
			"is_group": "1",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Asset"
		},
		{
			"account_name": "Rupiah Cash",
			"parent_number": "1110.000",
			"account_number": "1111.000",
			"is_group": "1",
			"account_currency": "IDR",
			"account_type": "Cash",
			"root_type": "Asset"
		},
		{
			"account_name": "House Bank General Cashier",
			"parent_number": "1111.000",
			"account_number": "1111.001",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Cash",
			"root_type": "Asset"
		},
		{
			"account_name": "House Bank Resto",
			"parent_number": "1111.000",
			"account_number": "1111.002",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Cash",
			"root_type": "Asset"
		},
		{
			"account_name": "House Bank Front Office",
			"parent_number": "1111.000",
			"account_number": "1111.003",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Cash",
			"root_type": "Asset"
		},
		{
			"account_name": "Other Currency Cash",
			"parent_number": "1110.000",
			"account_number": "1112.000",
			"is_group": "1",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Asset"
		},
		{
			"account_name": "USD Cash",
			"parent_number": "1112.000",
			"account_number": "1112.001",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Cash",
			"root_type": "Asset"
		},
		{
			"account_name": "Cash Clearance",
			"parent_number": "1110.000",
			"account_number": "1113.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Asset"
		},
		{
			"account_name": "Bank",
			"parent_number": "1100.000",
			"account_number": "1120.000",
			"is_group": "1",
			"account_currency": "IDR",
			"account_type": "Bank",
			"root_type": "Asset"
		},
		{
			"account_name": "Bank Rupiah",
			"parent_number": "1120.000",
			"account_number": "1121.000",
			"is_group": "1",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Asset"
		},
		{
			"account_name": "BCA",
			"parent_number": "1121.000",
			"account_number": "1121.001",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Bank",
			"root_type": "Asset"
		},
		{
			"account_name": "Bank Mandiri",
			"parent_number": "1121.000",
			"account_number": "1121.002",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Bank",
			"root_type": "Asset"
		},
		{
			"account_name": "Bank CIMB Niaga",
			"parent_number": "1121.000",
			"account_number": "1121.003",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Bank",
			"root_type": "Asset"
		},
		{
			"account_name": "Bank BRI",
			"parent_number": "1121.000",
			"account_number": "1121.004",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Bank",
			"root_type": "Asset"
		},
		{
			"account_name": "Bank BNI",
			"parent_number": "1121.000",
			"account_number": "1121.005",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Bank",
			"root_type": "Asset"
		},
		{
			"account_name": "Bank Other Currency",
			"parent_number": "1120.000",
			"account_number": "1122.000",
			"is_group": "1",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Asset"
		},
		{
			"account_name": "Account Receivable",
			"parent_number": "1100.000",
			"account_number": "1130.000",
			"is_group": "1",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Asset"
		},
		{
			"account_name": "A/R Bank",
			"parent_number": "1130.000",
			"account_number": "1131.000",
			"is_group": "1",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Asset"
		},
		{
			"account_name": "BCA Transfer",
			"parent_number": "1131.000",
			"account_number": "1131.001",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Receivable",
			"root_type": "Asset"
		},
		{
			"account_name": "Mandiri Transfer",
			"parent_number": "1131.000",
			"account_number": "1131.002",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Receivable",
			"root_type": "Asset"
		},
		{
			"account_name": "CIMB Transfer",
			"parent_number": "1131.000",
			"account_number": "1131.003",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Receivable",
			"root_type": "Asset"
		},
		{
			"account_name": "BRI Transfer",
			"parent_number": "1131.000",
			"account_number": "1131.004",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Receivable",
			"root_type": "Asset"
		},
		{
			"account_name": "BNI Transfer",
			"parent_number": "1131.000",
			"account_number": "1131.005",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Receivable",
			"root_type": "Asset"
		},
		{
			"account_name": "A/R Card and e-Payment",
			"parent_number": "1130.000",
			"account_number": "1132.000",
			"is_group": "1",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Asset"
		},
		{
			"account_name": "BCA EDC",
			"parent_number": "1132.000",
			"account_number": "1132.001",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Receivable",
			"root_type": "Asset"
		},
		{
			"account_name": "Mandiri EDC",
			"parent_number": "1132.000",
			"account_number": "1132.002",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Receivable",
			"root_type": "Asset"
		},
		{
			"account_name": "BRI EDC",
			"parent_number": "1132.000",
			"account_number": "1132.003",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Receivable",
			"root_type": "Asset"
		},
		{
			"account_name": "BNI EDC",
			"parent_number": "1132.000",
			"account_number": "1132.004",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Receivable",
			"root_type": "Asset"
		},
		{
			"account_name": "CIMB Niaga EDC",
			"parent_number": "1132.000",
			"account_number": "1132.005",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Receivable",
			"root_type": "Asset"
		},
		{
			"account_name": "OVO",
			"parent_number": "1132.000",
			"account_number": "1132.006",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Receivable",
			"root_type": "Asset"
		},
		{
			"account_name": "Dana",
			"parent_number": "1132.000",
			"account_number": "1132.007",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Receivable",
			"root_type": "Asset"
		},
		{
			"account_name": "Cashbac",
			"parent_number": "1132.000",
			"account_number": "1132.008",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Receivable",
			"root_type": "Asset"
		},
		{
			"account_name": "Other A/R",
			"parent_number": "1130.000",
			"account_number": "1133.000",
			"is_group": "1",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Asset"
		},
		{
			"account_name": "A/R City Ledger",
			"parent_number": "1133.000",
			"account_number": "1133.001",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Receivable",
			"root_type": "Asset"
		},
		{
			"account_name": "A/R Sale",
			"parent_number": "1133.000",
			"account_number": "1133.002",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Receivable",
			"root_type": "Asset"
		},
		{
			"account_name": "A/R Guest Ledger",
			"parent_number": "1133.000",
			"account_number": "1133.003",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Receivable",
			"root_type": "Asset"
		},
		{
			"account_name": "Inventory",
			"parent_number": "1100.000",
			"account_number": "1140.000",
			"is_group": "1",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Asset"
		},
		{
			"account_name": "Hotel Inventory",
			"parent_number": "1140.000",
			"account_number": "1141.000",
			"is_group": "1",
			"account_currency": "IDR",
			"account_type": "Stock",
			"root_type": "Asset"
		},
		{
			"account_name": "Store Inventory",
			"parent_number": "1141.000",
			"account_number": "1141.001",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Asset"
		},
		{
			"account_name": "House keeping Inventory",
			"parent_number": "1141.000",
			"account_number": "1141.002",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Stock",
			"root_type": "Asset"
		},
		{
			"account_name": "Engineering Inventory",
			"parent_number": "1141.000",
			"account_number": "1141.003",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Stock",
			"root_type": "Asset"
		},
		{
			"account_name": "Prepaid Expense",
			"parent_number": "1100.000",
			"account_number": "1150.000",
			"is_group": "1",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Asset"
		},
		{
			"account_name": "Prepaid Tax",
			"parent_number": "1150.000",
			"account_number": "1151.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Asset"
		},
		{
			"account_name": "Prepaid Rent",
			"parent_number": "1150.000",
			"account_number": "1152.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Asset"
		},
		{
			"account_name": "Other Prepaid",
			"parent_number": "1150.000",
			"account_number": "1153.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Asset"
		},
		{
			"account_name": "Temporary Account",
			"parent_number": "1100.000",
			"account_number": "1170.000",
			"is_group": "1",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Asset"
		},
		{
			"account_name": "Temporary Opening",
			"parent_number": "1170.000",
			"account_number": "1171.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Temporary",
			"root_type": "Asset"
		},
		{
			"account_name": "Deposit Customer",
			"parent_number": "1170.000",
			"account_number": "1172.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Asset"
		},
		{
			"account_name": "Fixed Asset",
			"parent_number": "1000.000",
			"account_number": "1200.000",
			"is_group": "1",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Asset"
		},
		{
			"account_name": "Asset",
			"parent_number": "1200.000",
			"account_number": "1210.000",
			"is_group": "1",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Asset"
		},
		{
			"account_name": "Property and Equipment",
			"parent_number": "1210.000",
			"account_number": "1211.000",
			"is_group": "1",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Asset"
		},
		{
			"account_name": "Land",
			"parent_number": "1211.000",
			"account_number": "1211.001",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Fixed Asset",
			"root_type": "Asset"
		},
		{
			"account_name": "Building",
			"parent_number": "1211.000",
			"account_number": "1211.002",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Fixed Asset",
			"root_type": "Asset"
		},
		{
			"account_name": "Vehicle",
			"parent_number": "1211.000",
			"account_number": "1211.003",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Fixed Asset",
			"root_type": "Asset"
		},
		{
			"account_name": "Computer and Hardware",
			"parent_number": "1211.000",
			"account_number": "1211.004",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Fixed Asset",
			"root_type": "Asset"
		},
		{
			"account_name": "Air Conditioning",
			"parent_number": "1211.000",
			"account_number": "1211.005",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Fixed Asset",
			"root_type": "Asset"
		},
		{
			"account_name": "Machinery",
			"parent_number": "1211.000",
			"account_number": "1211.006",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Fixed Asset",
			"root_type": "Asset"
		},
		{
			"account_name": "Electronic and Mechanical",
			"parent_number": "1211.000",
			"account_number": "1211.007",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Fixed Asset",
			"root_type": "Asset"
		},
		{
			"account_name": "Accumulated Depreciation of Asset",
			"parent_number": "1210.000",
			"account_number": "1212.000",
			"is_group": "1",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Asset"
		},
		{
			"account_name": "Accumulated Depreciation of Assets",
			"parent_number": "1212.000",
			"account_number": "1212.001",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Accumulated Depreciation",
			"root_type": "Asset"
		},
		{
			"account_name": "Furniture, Fixture and Equipment",
			"parent_number": "1210.000",
			"account_number": "1213.000",
			"is_group": "1",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Asset"
		},
		{
			"account_name": "FF&E Room",
			"parent_number": "1213.000",
			"account_number": "1213.001",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Fixed Asset",
			"root_type": "Asset"
		},
		{
			"account_name": "FF&E Food and Beverages",
			"parent_number": "1213.000",
			"account_number": "1213.002",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Fixed Asset",
			"root_type": "Asset"
		},
		{
			"account_name": "FF&E Human Resource",
			"parent_number": "1213.000",
			"account_number": "1213.003",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Fixed Asset",
			"root_type": "Asset"
		},
		{
			"account_name": "FF&E Sales and Marketing",
			"parent_number": "1213.000",
			"account_number": "1213.004",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Fixed Asset",
			"root_type": "Asset"
		},
		{
			"account_name": "FF&E Engineering",
			"parent_number": "1213.000",
			"account_number": "1213.005",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Fixed Asset",
			"root_type": "Asset"
		},
		{
			"account_name": "FF&E Administration and General",
			"parent_number": "1213.000",
			"account_number": "1213.006",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Fixed Asset",
			"root_type": "Asset"
		},
		{
			"account_name": "Operating Equipment",
			"parent_number": "1210.000",
			"account_number": "1214.000",
			"is_group": "1",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Asset"
		},
		{
			"account_name": "Opr. Eqp Linen Room",
			"parent_number": "1214.000",
			"account_number": "1214.001",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Fixed Asset",
			"root_type": "Asset"
		},
		{
			"account_name": "Opr. Eqp Linen FB",
			"parent_number": "1214.000",
			"account_number": "1214.002",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Fixed Asset",
			"root_type": "Asset"
		},
		{
			"account_name": "Opr. Eqp Chinaware Room",
			"parent_number": "1214.000",
			"account_number": "1214.003",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Fixed Asset",
			"root_type": "Asset"
		},
		{
			"account_name": "Opr. Eqp Chinaware FB",
			"parent_number": "1214.000",
			"account_number": "1214.004",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Fixed Asset",
			"root_type": "Asset"
		},
		{
			"account_name": "Opr. Eqp Glassware Room",
			"parent_number": "1214.000",
			"account_number": "1214.005",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Fixed Asset",
			"root_type": "Asset"
		},
		{
			"account_name": "Opr. Eqp Glassware FB",
			"parent_number": "1214.000",
			"account_number": "1214.006",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Fixed Asset",
			"root_type": "Asset"
		},
		{
			"account_name": "Opr. Eqp Silverware Room",
			"parent_number": "1214.000",
			"account_number": "1214.007",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Fixed Asset",
			"root_type": "Asset"
		},
		{
			"account_name": "Opr. Eqp Silverware FB",
			"parent_number": "1214.000",
			"account_number": "1214.008",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Fixed Asset",
			"root_type": "Asset"
		},
		{
			"account_name": "Opr. Eqp Kitchen Utensils",
			"parent_number": "1214.000",
			"account_number": "1214.009",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Fixed Asset",
			"root_type": "Asset"
		},
		{
			"account_name": "Opr. Eqp Uniform Room",
			"parent_number": "1214.000",
			"account_number": "1214.010",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Fixed Asset",
			"root_type": "Asset"
		},
		{
			"account_name": "Opr. Eqp Uniform FB",
			"parent_number": "1214.000",
			"account_number": "1214.011",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Fixed Asset",
			"root_type": "Asset"
		},
		{
			"account_name": "Opr. Eqp Administration & General",
			"parent_number": "1214.000",
			"account_number": "1214.012",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Fixed Asset",
			"root_type": "Asset"
		},
		{
			"account_name": "Opr. Eqp Human Resource",
			"parent_number": "1214.000",
			"account_number": "1214.013",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Fixed Asset",
			"root_type": "Asset"
		},
		{
			"account_name": "Opr. Eqp Sales and Marketing",
			"parent_number": "1214.000",
			"account_number": "1214.014",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Fixed Asset",
			"root_type": "Asset"
		},
		{
			"account_name": "Opr. Eqp Room",
			"parent_number": "1214.000",
			"account_number": "1214.015",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Fixed Asset",
			"root_type": "Asset"
		},
		{
			"account_name": "Opr. Eqp House Keeping",
			"parent_number": "1214.000",
			"account_number": "1214.016",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Fixed Asset",
			"root_type": "Asset"
		},
		{
			"account_name": "Opr. Eqp Resto",
			"parent_number": "1214.000",
			"account_number": "1214.017",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Fixed Asset",
			"root_type": "Asset"
		},
		{
			"account_name": "Opr. Eqp Other",
			"parent_number": "1214.000",
			"account_number": "1214.018",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Fixed Asset",
			"root_type": "Asset"
		},
		{
			"account_name": "Liabilities",
			"parent_number": "",
			"account_number": "2000.000",
			"is_group": "1",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Liability"
		},
		{
			"account_name": "Current Liabilities",
			"parent_number": "2000.000",
			"account_number": "2100.000",
			"is_group": "1",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Liability"
		},
		{
			"account_name": "Account Payable",
			"parent_number": "2100.000",
			"account_number": "2110.000",
			"is_group": "1",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Liability"
		},
		{
			"account_name": "Stock Received But Not Billed",
			"parent_number": "2110.000",
			"account_number": "2110.003",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Stock Received But Not Billed",
			"root_type": "Liability"
		},
		{
			"account_name": "A/P Trade",
			"parent_number": "2110.000",
			"account_number": "2110.001",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Payable",
			"root_type": "Liability"
		},
		{
			"account_name": "A/P Short Term Loan",
			"parent_number": "2110.000",
			"account_number": "2110.002",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Payable",
			"root_type": "Liability"
		},
		{
			"account_name": "A/P Service Charge",
			"parent_number": "2110.000",
			"account_number": "2110.004",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Liability"
		},
		{
			"account_name": "A/P Guest Deposit",
			"parent_number": "2110.000",
			"account_number": "2110.005",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Payable",
			"root_type": "Liability"
		},
		{
			"account_name": "A/P Loss and Breakage - 5%",
			"parent_number": "2110.000",
			"account_number": "2110.006",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Payable",
			"root_type": "Liability"
		},
		{
			"account_name": "A/P HR Development - 2%",
			"parent_number": "2110.000",
			"account_number": "2110.007",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Payable",
			"root_type": "Liability"
		},
		{
			"account_name": "A/P Payable Commission",
			"parent_number": "2110.000",
			"account_number": "2110.008",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Payable",
			"root_type": "Liability"
		},
		{
			"account_name": "A/P Tips",
			"parent_number": "2110.000",
			"account_number": "2110.009",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Payable",
			"root_type": "Liability"
		},
		{
			"account_name": "A/P Clearance",
			"parent_number": "2110.000",
			"account_number": "2110.010",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Payable",
			"root_type": "Liability"
		},
		{
			"account_name": "A/P Owner",
			"parent_number": "2110.000",
			"account_number": "2110.011",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Payable",
			"root_type": "Liability"
		},
		{
			"account_name": "A/P Other",
			"parent_number": "2110.000",
			"account_number": "2110.012",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Payable",
			"root_type": "Liability"
		},
		{
			"account_name": "A/P In Transit",
			"parent_number": "2110.000",
			"account_number": "2110.013",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Payable",
			"root_type": "Liability"
		},
		{
			"account_name": "Prepaid Income",
			"parent_number": "2100.000",
			"account_number": "2120.000",
			"is_group": "1",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Liability"
		},
		{
			"account_name": "Prepaid Income",
			"parent_number": "2120.000",
			"account_number": "2121.000",
			"is_group": "1",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Liability"
		},
		{
			"account_name": "DP Sales",
			"parent_number": "2121.000",
			"account_number": "2121.001",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Bank",
			"root_type": "Liability"
		},
		{
			"account_name": "DP Room",
			"parent_number": "2121.000",
			"account_number": "2121.002",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Liability"
		},
		{
			"account_name": "Accrued Expense",
			"parent_number": "2100.000",
			"account_number": "2130.000",
			"is_group": "1",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Liability"
		},
		{
			"account_name": "Accrued Expense",
			"parent_number": "2130.000",
			"account_number": "2131.000",
			"is_group": "1",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Liability"
		},
		{
			"account_name": "A/E Electricity",
			"parent_number": "2131.000",
			"account_number": "2131.001",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Liability"
		},
		{
			"account_name": "A/E Contract Agreement",
			"parent_number": "2131.000",
			"account_number": "2131.033",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Liability"
		},
		{
			"account_name": "A/E Telephone",
			"parent_number": "2131.000",
			"account_number": "2131.002",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Liability"
		},
		{
			"account_name": "A/E Water",
			"parent_number": "2131.000",
			"account_number": "2131.003",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Liability"
		},
		{
			"account_name": "A/E Internet",
			"parent_number": "2131.000",
			"account_number": "2131.004",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Liability"
		},
		{
			"account_name": "A/E Salary",
			"parent_number": "2131.000",
			"account_number": "2131.005",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Liability"
		},
		{
			"account_name": "A/E Insurance",
			"parent_number": "2131.000",
			"account_number": "2131.006",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Liability"
		},
		{
			"account_name": "A/E Medical",
			"parent_number": "2131.000",
			"account_number": "2131.007",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Liability"
		},
		{
			"account_name": "A/E Jamsostek",
			"parent_number": "2131.000",
			"account_number": "2131.008",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Liability"
		},
		{
			"account_name": "A/E TV Channel",
			"parent_number": "2131.000",
			"account_number": "2131.009",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Liability"
		},
		{
			"account_name": "A/E Laundry",
			"parent_number": "2131.000",
			"account_number": "2131.010",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Liability"
		},
		{
			"account_name": "A/E Meal",
			"parent_number": "2131.000",
			"account_number": "2131.011",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Liability"
		},
		{
			"account_name": "A/E Music and Entertainment",
			"parent_number": "2131.000",
			"account_number": "2131.012",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Liability"
		},
		{
			"account_name": "A/E Newspaper and Magazine",
			"parent_number": "2131.000",
			"account_number": "2131.013",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Liability"
		},
		{
			"account_name": "A/E Transportation",
			"parent_number": "2131.000",
			"account_number": "2131.014",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Liability"
		},
		{
			"account_name": "A/E Commission",
			"parent_number": "2131.000",
			"account_number": "2131.015",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Liability"
		},
		{
			"account_name": "A/E Audit",
			"parent_number": "2131.000",
			"account_number": "2131.016",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Liability"
		},
		{
			"account_name": "A/E Pest Control",
			"parent_number": "2131.000",
			"account_number": "2131.017",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Liability"
		},
		{
			"account_name": "A/E Garbage Cleaning",
			"parent_number": "2131.000",
			"account_number": "2131.018",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Liability"
		},
		{
			"account_name": "A/E Removal of Waste",
			"parent_number": "2131.000",
			"account_number": "2131.019",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Liability"
		},
		{
			"account_name": "A/E Elevator",
			"parent_number": "2131.000",
			"account_number": "2131.020",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Liability"
		},
		{
			"account_name": "A/E S&M Fee",
			"parent_number": "2131.000",
			"account_number": "2131.021",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Liability"
		},
		{
			"account_name": "A/E Incentive Fee",
			"parent_number": "2131.000",
			"account_number": "2131.022",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Liability"
		},
		{
			"account_name": "A/E Management Fee",
			"parent_number": "2131.000",
			"account_number": "2131.023",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Liability"
		},
		{
			"account_name": "A/E Room Department",
			"parent_number": "2131.000",
			"account_number": "2131.024",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Liability"
		},
		{
			"account_name": "A/E FB Department",
			"parent_number": "2131.000",
			"account_number": "2131.025",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Liability"
		},
		{
			"account_name": "A/E HR Department",
			"parent_number": "2131.000",
			"account_number": "2131.026",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Liability"
		},
		{
			"account_name": "A/E Accounting Department",
			"parent_number": "2131.000",
			"account_number": "2131.027",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Liability"
		},
		{
			"account_name": "A/E Sales and Marketing Department",
			"parent_number": "2131.000",
			"account_number": "2131.028",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Liability"
		},
		{
			"account_name": "A/E Engineering Department",
			"parent_number": "2131.000",
			"account_number": "2131.029",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Liability"
		},
		{
			"account_name": "A/E Security Department",
			"parent_number": "2131.000",
			"account_number": "2131.030",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Liability"
		},
		{
			"account_name": "A/E Contract Cleaning",
			"parent_number": "2131.000",
			"account_number": "2131.031",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Liability"
		},
		{
			"account_name": "A/E Petty Cash",
			"parent_number": "2131.000",
			"account_number": "2131.032",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Liability"
		},
		{
			"account_name": "A/E Daily Worker",
			"parent_number": "2131.000",
			"account_number": "2131.034",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Liability"
		},
		{
			"account_name": "A/E Outsourcing",
			"parent_number": "2131.000",
			"account_number": "2131.035",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Liability"
		},
		{
			"account_name": "A/E Other",
			"parent_number": "2131.000",
			"account_number": "2131.036",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Liability"
		},
		{
			"account_name": "Tax Payable",
			"parent_number": "2100.000",
			"account_number": "2140.000",
			"is_group": "1",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Liability"
		},
		{
			"account_name": "Reconstruction Tax - PB 1",
			"parent_number": "2140.000",
			"account_number": "2141.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Tax",
			"root_type": "Liability"
		},
		{
			"account_name": "Land & Building Tax",
			"parent_number": "2140.000",
			"account_number": "2142.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Tax",
			"root_type": "Liability"
		},
		{
			"account_name": "Fixed Asset",
			"parent_number": "2000.000",
			"account_number": "2200.000",
			"is_group": "1",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Liability"
		},
		{
			"account_name": "Debt to Third Parties",
			"parent_number": "2200.000",
			"account_number": "2210.000",
			"is_group": "1",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Liability"
		},
		{
			"account_name": "Routine Third Party Loan",
			"parent_number": "2210.000",
			"account_number": "2211.000",
			"is_group": "1",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Liability"
		},
		{
			"account_name": "Shareholder Loan",
			"parent_number": "2211.000",
			"account_number": "2211.001",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Liability"
		},
		{
			"account_name": "Routine Loan",
			"parent_number": "2211.000",
			"account_number": "2211.002",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Liability"
		},
		{
			"account_name": "Non-routine Third Party Loan",
			"parent_number": "2210.000",
			"account_number": "2212.000",
			"is_group": "1",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Liability"
		},
		{
			"account_name": "Shareholder Loan",
			"parent_number": "2212.000",
			"account_number": "2212.001",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Liability"
		},
		{
			"account_name": "Non-routine Loan",
			"parent_number": "2212.000",
			"account_number": "2212.002",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Liability"
		},
		{
			"account_name": "Non-routine Third Party Loan Interest Debt",
			"parent_number": "2210.000",
			"account_number": "2213.000",
			"is_group": "1",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Liability"
		},
		{
			"account_name": "Interest Debt",
			"parent_number": "2213.000",
			"account_number": "2213.001",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Liability"
		},
		{
			"account_name": "Debt to Bank",
			"parent_number": "2200.000",
			"account_number": "2220.000",
			"is_group": "1",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Liability"
		},
		{
			"account_name": "Bank Loan",
			"parent_number": "2220.000",
			"account_number": "2221.000",
			"is_group": "1",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Liability"
		},
		{
			"account_name": "Bank Loan",
			"parent_number": "2221.000",
			"account_number": "2221.001",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Liability"
		},
		{
			"account_name": "Leasing Debt",
			"parent_number": "2200.000",
			"account_number": "2230.000",
			"is_group": "1",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Liability"
		},
		{
			"account_name": "Leasing Debt",
			"parent_number": "2230.000",
			"account_number": "2231.000",
			"is_group": "1",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Liability"
		},
		{
			"account_name": "Vehicle Leasing",
			"parent_number": "2231.000",
			"account_number": "2231.001",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Liability"
		},
		{
			"account_name": "Other Leasing",
			"parent_number": "2231.000",
			"account_number": "2231.002",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Liability"
		},
		{
			"account_name": "Other Debt",
			"parent_number": "2200.000",
			"account_number": "2240.000",
			"is_group": "1",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Liability"
		},
		{
			"account_name": "Other Debt",
			"parent_number": "2240.000",
			"account_number": "2241.000",
			"is_group": "1",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Liability"
		},
		{
			"account_name": "Debt",
			"parent_number": "2241.000",
			"account_number": "2241.001",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Liability"
		},
		{
			"account_name": "Capital",
			"parent_number": "",
			"account_number": "3000.000",
			"is_group": "1",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Equity"
		},
		{
			"account_name": "Capital",
			"parent_number": "3000.000",
			"account_number": "3100.000",
			"is_group": "1",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Equity"
		},
		{
			"account_name": "Paid Up Capital",
			"parent_number": "3100.000",
			"account_number": "3110.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Equity"
		},
		{
			"account_name": "Shareholder",
			"parent_number": "3100.000",
			"account_number": "3120.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Equity"
		},
		{
			"account_name": "Opening Balance of Equity",
			"parent_number": "3100.000",
			"account_number": "3130.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Equity"
		},
		{
			"account_name": "Withdrawal",
			"parent_number": "3100.000",
			"account_number": "3140.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Equity"
		},
		{
			"account_name": "Earning",
			"parent_number": "3000.000",
			"account_number": "3200.000",
			"is_group": "1",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Equity"
		},
		{
			"account_name": "Retained Earning",
			"parent_number": "3200.000",
			"account_number": "3210.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Equity"
		},
		{
			"account_name": "Profit and Loss Current Period",
			"parent_number": "3200.000",
			"account_number": "3220.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Equity"
		},
		{
			"account_name": "Profit and Loss Last Year",
			"parent_number": "3200.000",
			"account_number": "3230.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Equity"
		},
		{
			"account_name": "Prior Year Adjustment",
			"parent_number": "3200.000",
			"account_number": "3240.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Equity"
		},
		{
			"account_name": "Revenue",
			"parent_number": "",
			"account_number": "4000.000",
			"is_group": "1",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Income"
		},
		{
			"account_name": "Food and Beverages Revenue",
			"parent_number": "4000.000",
			"account_number": "4100.000",
			"is_group": "1",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Income"
		},
		{
			"account_name": "Kitchen Revenue",
			"parent_number": "4100.000",
			"account_number": "4110.000",
			"is_group": "1",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Income"
		},
		{
			"account_name": "Breakfast Revenue",
			"parent_number": "4110.000",
			"account_number": "4110.001",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Income Account",
			"root_type": "Income"
		},
		{
			"account_name": "Restaurant Revenue",
			"parent_number": "4100.000",
			"account_number": "4120.000",
			"is_group": "1",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Income"
		},
		{
			"account_name": "Restaurant Food Revenue",
			"parent_number": "4120.000",
			"account_number": "4120.001",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Income Account",
			"root_type": "Income"
		},
		{
			"account_name": "Restaurant Beverages Revenue",
			"parent_number": "4120.000",
			"account_number": "4120.002",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Income Account",
			"root_type": "Income"
		},
		{
			"account_name": "Lounge Revenue",
			"parent_number": "4100.000",
			"account_number": "4130.000",
			"is_group": "1",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Income"
		},
		{
			"account_name": "Lounge Food Revenue",
			"parent_number": "4130.000",
			"account_number": "4130.001",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Income Account",
			"root_type": "Income"
		},
		{
			"account_name": "Lounge Beverages Revenue",
			"parent_number": "4130.000",
			"account_number": "4130.002",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Income Account",
			"root_type": "Income"
		},
		{
			"account_name": "Room Service Revenue",
			"parent_number": "4100.000",
			"account_number": "4140.000",
			"is_group": "1",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Income"
		},
		{
			"account_name": "Room Service Food Revenue",
			"parent_number": "4140.000",
			"account_number": "4140.001",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Income Account",
			"root_type": "Income"
		},
		{
			"account_name": "Room Service Beverages Revenue",
			"parent_number": "4140.000",
			"account_number": "4140.002",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Income Account",
			"root_type": "Income"
		},
		{
			"account_name": "Banquet Revenue",
			"parent_number": "4100.000",
			"account_number": "4150.000",
			"is_group": "1",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Income"
		},
		{
			"account_name": "Banquet Lunch Revenue",
			"parent_number": "4150.000",
			"account_number": "4150.001",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Income Account",
			"root_type": "Income"
		},
		{
			"account_name": "Banquet Dinner Revenue",
			"parent_number": "4150.000",
			"account_number": "4150.002",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Income Account",
			"root_type": "Income"
		},
		{
			"account_name": "Banquet Coffee Break Revenue",
			"parent_number": "4150.000",
			"account_number": "4150.003",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Income Account",
			"root_type": "Income"
		},
		{
			"account_name": "Other Food and Beverages Revenue",
			"parent_number": "4100.000",
			"account_number": "4160.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Income Account",
			"root_type": "Income"
		},
		{
			"account_name": "Room Revenue",
			"parent_number": "4000.000",
			"account_number": "4200.000",
			"is_group": "1",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Income"
		},
		{
			"account_name": "Front Office Revenue",
			"parent_number": "4200.000",
			"account_number": "4210.000",
			"is_group": "1",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Income"
		},
		{
			"account_name": "Room Revenue",
			"parent_number": "4210.000",
			"account_number": "4210.001",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Income Account",
			"root_type": "Income"
		},
		{
			"account_name": "House Keeping Revenue",
			"parent_number": "4200.000",
			"account_number": "4220.000",
			"is_group": "1",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Income"
		},
		{
			"account_name": "Guest Laundry Revenue",
			"parent_number": "4220.000",
			"account_number": "4220.001",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Income Account",
			"root_type": "Income"
		},
		{
			"account_name": "Public Laundry Revenue",
			"parent_number": "4220.000",
			"account_number": "4220.002",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Income Account",
			"root_type": "Income"
		},
		{
			"account_name": "Other Room Revenue",
			"parent_number": "4200.000",
			"account_number": "4230.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Income Account",
			"root_type": "Income"
		},
		{
			"account_name": "Other Revenue",
			"parent_number": "4000.000",
			"account_number": "4300.000",
			"is_group": "1",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Income"
		},
		{
			"account_name": "Rounding Off",
			"parent_number": "4300.000",
			"account_number": "4300.001",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Income Account",
			"root_type": "Income"
		},
		{
			"account_name": "Foreign Exchange Earned",
			"parent_number": "4300.000",
			"account_number": "4300.002",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Income Account",
			"root_type": "Income"
		},
		{
			"account_name": "Interest Income",
			"parent_number": "4300.000",
			"account_number": "4300.003",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Income Account",
			"root_type": "Income"
		},
		{
			"account_name": "Cost of Sale",
			"parent_number": "",
			"account_number": "5000.000",
			"is_group": "1",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Expense"
		},
		{
			"account_name": "Food and Beverage Cost",
			"parent_number": "5000.000",
			"account_number": "5100.000",
			"is_group": "1",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Expense"
		},
		{
			"account_name": "Food Cost",
			"parent_number": "5100.000",
			"account_number": "5110.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Cost of Goods Sold",
			"root_type": "Expense"
		},
		{
			"account_name": "Beverage Cost",
			"parent_number": "5100.000",
			"account_number": "5120.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Cost of Goods Sold",
			"root_type": "Expense"
		},
		{
			"account_name": "Room Cost",
			"parent_number": "5000.000",
			"account_number": "5200.000",
			"is_group": "1",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Expense"
		},
		{
			"account_name": "Cost of Front Office",
			"parent_number": "5200.000",
			"account_number": "5210.000",
			"is_group": "1",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Expense"
		},
		{
			"account_name": "Cost of Guest Supplies",
			"parent_number": "5210.000",
			"account_number": "5210.001",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Cost of Goods Sold",
			"root_type": "Expense"
		},
		{
			"account_name": "Cost of House Keeping",
			"parent_number": "5200.000",
			"account_number": "5220.000",
			"is_group": "1",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Expense"
		},
		{
			"account_name": "Cost of Laundry",
			"parent_number": "5220.000",
			"account_number": "5220.001",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Expense"
		},
		{
			"account_name": "Other Room Cost",
			"parent_number": "5200.000",
			"account_number": "5230.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Expense"
		},
		{
			"account_name": "Payroll",
			"parent_number": "",
			"account_number": "6000.000",
			"is_group": "1",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Expense"
		},
		{
			"account_name": "Salary and Wages",
			"parent_number": "6000.000",
			"account_number": "6100.000",
			"is_group": "1",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Expense"
		},
		{
			"account_name": "F&B Department Salary",
			"parent_number": "6100.000",
			"account_number": "6101.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Expense Account",
			"root_type": "Expense"
		},
		{
			"account_name": "Room Department Salary",
			"parent_number": "6100.000",
			"account_number": "6102.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Equity",
			"root_type": "Expense"
		},
		{
			"account_name": "Sales and Marketing Department Salary",
			"parent_number": "6100.000",
			"account_number": "6103.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Expense Account",
			"root_type": "Expense"
		},
		{
			"account_name": "HR Department Salary",
			"parent_number": "6100.000",
			"account_number": "6104.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Expense Account",
			"root_type": "Expense"
		},
		{
			"account_name": "Engineering Department Salary",
			"parent_number": "6100.000",
			"account_number": "6105.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Expense Account",
			"root_type": "Expense"
		},
		{
			"account_name": "Accounting Department Salary",
			"parent_number": "6100.000",
			"account_number": "6106.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Expense Account",
			"root_type": "Expense"
		},
		{
			"account_name": "Security Department Salary",
			"parent_number": "6100.000",
			"account_number": "6107.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Expense Account",
			"root_type": "Expense"
		},
		{
			"account_name": "Corporate Department Salary",
			"parent_number": "6100.000",
			"account_number": "6108.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Expense Account",
			"root_type": "Expense"
		},
		{
			"account_name": "Daily Worker Wages",
			"parent_number": "6100.000",
			"account_number": "6109.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Expense Account",
			"root_type": "Expense"
		},
		{
			"account_name": "Employee Benefit",
			"parent_number": "6000.000",
			"account_number": "6200.000",
			"is_group": "1",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Expense"
		},
		{
			"account_name": "Employee Insurance Cost",
			"parent_number": "6200.000",
			"account_number": "6201.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Expense Account",
			"root_type": "Expense"
		},
		{
			"account_name": "Employee Medical Expense",
			"parent_number": "6200.000",
			"account_number": "6202.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Expense Account",
			"root_type": "Expense"
		},
		{
			"account_name": "Employee Meal Expense",
			"parent_number": "6200.000",
			"account_number": "6203.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Expense Account",
			"root_type": "Expense"
		},
		{
			"account_name": "THR Cost, Benefits, Commission",
			"parent_number": "6200.000",
			"account_number": "6204.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Expense Account",
			"root_type": "Expense"
		},
		{
			"account_name": "Uniform Cost",
			"parent_number": "6200.000",
			"account_number": "6205.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Expense Account",
			"root_type": "Expense"
		},
		{
			"account_name": "Training Cost",
			"parent_number": "6200.000",
			"account_number": "6206.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Expense Account",
			"root_type": "Expense"
		},
		{
			"account_name": "Entertainment Expense",
			"parent_number": "6200.000",
			"account_number": "6207.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Expense Account",
			"root_type": "Expense"
		},
		{
			"account_name": "Other Employee Cost",
			"parent_number": "6200.000",
			"account_number": "6208.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Expense Account",
			"root_type": "Expense"
		},
		{
			"account_name": "Expense",
			"parent_number": "",
			"account_number": "7000.000",
			"is_group": "1",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Expense"
		},
		{
			"account_name": "Operational Supplies",
			"parent_number": "7000.000",
			"account_number": "7100.000",
			"is_group": "1",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Expense"
		},
		{
			"account_name": "Paper Supplies",
			"parent_number": "7100.000",
			"account_number": "7101.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Expense Account",
			"root_type": "Expense"
		},
		{
			"account_name": "Print and Stationary",
			"parent_number": "7100.000",
			"account_number": "7102.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Expense Account",
			"root_type": "Expense"
		},
		{
			"account_name": "Office Supplies",
			"parent_number": "7100.000",
			"account_number": "7103.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Expense Account",
			"root_type": "Expense"
		},
		{
			"account_name": "Cleaning Supplies",
			"parent_number": "7100.000",
			"account_number": "7104.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Expense Account",
			"root_type": "Expense"
		},
		{
			"account_name": "Gas",
			"parent_number": "7100.000",
			"account_number": "7105.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Expense Account",
			"root_type": "Expense"
		},
		{
			"account_name": "FB Supplies",
			"parent_number": "7100.000",
			"account_number": "7106.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Expense Account",
			"root_type": "Expense"
		},
		{
			"account_name": "Room Supplies",
			"parent_number": "7100.000",
			"account_number": "7107.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Expense Account",
			"root_type": "Expense"
		},
		{
			"account_name": "Sales Supplies",
			"parent_number": "7100.000",
			"account_number": "7108.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Expense Account",
			"root_type": "Expense"
		},
		{
			"account_name": "Building and Office Expense",
			"parent_number": "7000.000",
			"account_number": "7200.000",
			"is_group": "1",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Expense"
		},
		{
			"account_name": "Electricity",
			"parent_number": "7200.000",
			"account_number": "7201.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Expense Account",
			"root_type": "Expense"
		},
		{
			"account_name": "Water and Sewage",
			"parent_number": "7200.000",
			"account_number": "7202.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Expense Account",
			"root_type": "Expense"
		},
		{
			"account_name": "Telephone",
			"parent_number": "7200.000",
			"account_number": "7203.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Expense Account",
			"root_type": "Expense"
		},
		{
			"account_name": "Internet",
			"parent_number": "7200.000",
			"account_number": "7204.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Expense Account",
			"root_type": "Expense"
		},
		{
			"account_name": "TV Cable & Satellite",
			"parent_number": "7200.000",
			"account_number": "7205.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Expense Account",
			"root_type": "Expense"
		},
		{
			"account_name": "Pest Control",
			"parent_number": "7200.000",
			"account_number": "7206.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Expense Account",
			"root_type": "Expense"
		},
		{
			"account_name": "Air Conditioning",
			"parent_number": "7200.000",
			"account_number": "7207.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Expense Account",
			"root_type": "Expense"
		},
		{
			"account_name": "Elevator and Escalator",
			"parent_number": "7200.000",
			"account_number": "7208.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Expense Account",
			"root_type": "Expense"
		},
		{
			"account_name": "Furniture",
			"parent_number": "7200.000",
			"account_number": "7209.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Expense Account",
			"root_type": "Expense"
		},
		{
			"account_name": "Garbage Cleaning",
			"parent_number": "7200.000",
			"account_number": "7210.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Expense Account",
			"root_type": "Expense"
		},
		{
			"account_name": "Cleaning Equipment",
			"parent_number": "7200.000",
			"account_number": "7211.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Expense Account",
			"root_type": "Expense"
		},
		{
			"account_name": "Building Maintenance",
			"parent_number": "7200.000",
			"account_number": "7212.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Expense Account",
			"root_type": "Expense"
		},
		{
			"account_name": "Mechanical and Electrical Equipment",
			"parent_number": "7200.000",
			"account_number": "7213.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Expense Account",
			"root_type": "Expense"
		},
		{
			"account_name": "Other Building and Office Expense",
			"parent_number": "7200.000",
			"account_number": "7214.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Expense Account",
			"root_type": "Expense"
		},
		{
			"account_name": "General Expense",
			"parent_number": "7000.000",
			"account_number": "7300.000",
			"is_group": "1",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Expense"
		},
		{
			"account_name": "Fuel",
			"parent_number": "7300.000",
			"account_number": "7301.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Expense Account",
			"root_type": "Expense"
		},
		{
			"account_name": "Parking",
			"parent_number": "7300.000",
			"account_number": "7302.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Expense Account",
			"root_type": "Expense"
		},
		{
			"account_name": "Transportation",
			"parent_number": "7300.000",
			"account_number": "7303.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Expense Account",
			"root_type": "Expense"
		},
		{
			"account_name": "Postage",
			"parent_number": "7300.000",
			"account_number": "7304.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Expense Account",
			"root_type": "Expense"
		},
		{
			"account_name": "Vehicle Repair Expense",
			"parent_number": "7300.000",
			"account_number": "7305.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Expense Account",
			"root_type": "Expense"
		},
		{
			"account_name": "Stock Adjustment",
			"parent_number": "7300.000",
			"account_number": "7306.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Stock Adjustment",
			"root_type": "Expense"
		},
		{
			"account_name": "China, Glassware, Silver, Linen Expense",
			"parent_number": "7000.000",
			"account_number": "7400.000",
			"is_group": "1",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Expense"
		},
		{
			"account_name": "China Expense",
			"parent_number": "7400.000",
			"account_number": "7401.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Expense Account",
			"root_type": "Expense"
		},
		{
			"account_name": "Glassware Expense",
			"parent_number": "7400.000",
			"account_number": "7402.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Expense Account",
			"root_type": "Expense"
		},
		{
			"account_name": "Silver Expense",
			"parent_number": "7400.000",
			"account_number": "7403.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Expense Account",
			"root_type": "Expense"
		},
		{
			"account_name": "Linen Expense",
			"parent_number": "7400.000",
			"account_number": "7404.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Expense Account",
			"root_type": "Expense"
		},
		{
			"account_name": "Information System Expense",
			"parent_number": "7000.000",
			"account_number": "7500.000",
			"is_group": "1",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Expense"
		},
		{
			"account_name": "Hardware Expense",
			"parent_number": "7500.000",
			"account_number": "7501.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Expense Account",
			"root_type": "Expense"
		},
		{
			"account_name": "Software Expense",
			"parent_number": "7500.000",
			"account_number": "7502.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Expense Account",
			"root_type": "Expense"
		},
		{
			"account_name": "IT Consultant Expense",
			"parent_number": "7500.000",
			"account_number": "7503.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Expense Account",
			"root_type": "Expense"
		},
		{
			"account_name": "Other Information System Expense",
			"parent_number": "7500.000",
			"account_number": "7504.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Expense Account",
			"root_type": "Expense"
		},
		{
			"account_name": "Other Expense",
			"parent_number": "7000.000",
			"account_number": "7600.000",
			"is_group": "1",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Expense"
		},
		{
			"account_name": "Administration Bank",
			"parent_number": "7600.000",
			"account_number": "7601.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Expense Account",
			"root_type": "Expense"
		},
		{
			"account_name": "Land and Building Tax (PBB)",
			"parent_number": "7600.000",
			"account_number": "7602.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Tax",
			"root_type": "Expense"
		},
		{
			"account_name": "Income Tax",
			"parent_number": "7600.000",
			"account_number": "7603.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Tax",
			"root_type": "Expense"
		},
		{
			"account_name": "PPN Tax",
			"parent_number": "7600.000",
			"account_number": "7604.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Tax",
			"root_type": "Expense"
		},
		{
			"account_name": "Depreciation",
			"parent_number": "7600.000",
			"account_number": "7605.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Depreciation",
			"root_type": "Expense"
		},
		{
			"account_name": "Round Off",
			"parent_number": "7600.000",
			"account_number": "7607.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "Round Off",
			"root_type": "Expense"
		},
		{
			"account_name": "Write Off",
			"parent_number": "7600.000",
			"account_number": "7608.000",
			"is_group": "0",
			"account_currency": "IDR",
			"account_type": "",
			"root_type": "Expense"
		}
	]
	return accounts
