CREATE TABLE [Watermark] (
  [ViewName] varchar(20) PRIMARY KEY,
  [LastExecution] datetime NOT NULL,
  [Retries] smallint NOT NULL,
  [LastErrorDate] datetime,
  [LastErrorResponse] text,
  [LastErrorInputPayload] text,
  [LastResponse] text
)
GO

CREATE TABLE [VWCrm_ContactMaster] (
  [ContactID] int NOT NULL,
  [ssn] varchar(9),
  [SSNFlag] smallint,
  [ContactName] varchar(80) NOT NULL,
  [DateOfBirth] datetime,
  [DateOfDeath] datetime,
  [ActiveFlag] smallint,
  [PrimaryLastName] varchar(20),
  [PrimaryFirstName] varchar(12),
  [PrimaryMiddleInitial] varchar(20),
  [PrimaryGender] varchar(4),
  [DisbursementEligibilityFlag] smallint NOT NULL,
  [ValidFrom] datetime2 NOT NULL,
  PRIMARY KEY ([ContactID])
)
GO

CREATE TABLE [VWCrm_ContactPhones] (
  [ContactID] int NOT NULL,
  [INNO_ID] int NOT NULL,
  [PhoneNumber] char(25) NOT NULL,
  [PrimaryPhoneNumberFlag] smallint NOT NULL,
  [PhoneTypeCode] char(8) NOT NULL,
  [ValidFrom] datetime2 NOT NULL,
  PRIMARY KEY ([INNO_ID])
)
GO

CREATE TABLE [VWCrm_Addresses] (
  [INNO_ID] int NOT NULL,
  [ContactID] int NOT NULL,
  [Address1] varchar(40),
  [AddressType] smallint NOT NULL,
  [Address2] varchar(40),
  [Address3] varchar(40),
  [City] varchar(30),
  [State] char(2),
  [ZipCode] char(10),
  [CountryCode] char(2),
  [primaryaddressflag] smallint,
  [ValidFrom] datetime2 NOT NULL,
  PRIMARY KEY ([INNO_ID])
)
GO

CREATE TABLE [VWCrm_AccountMaster] (
  [CustomerAccountNumber] varchar(14) NOT NULL,
  [OwnerContactID] int NOT NULL,
  [AccountTierLevelNum] int,
  [AccountTierLevelDesc] varchar(30),
  [AccountTypeCode] varchar(4) NOT NULL,
  [AccountTypeDescription] varchar(30) NOT NULL,
  [AccountCategoryCode] varchar(4) NOT NULL,
  [AccountCategoryDescription] varchar(30) NOT NULL,
  [FreezeCode] varchar(8),
  [FreezeDesc] varchar(50),
  [AdminOfficerContactID] int,
  [AdministratorName] varchar(80),
  [ActiveFlag] smallint NOT NULL,
  [DateOpened] datetime,
  [ClosedDate] datetime,
  [ClosedFlag] smallint NOT NULL,
  [CustomerDescriptionLine1] varchar(40),
  [CustomerDescriptionLine2] varchar(40),
  [CustomerDescriptionLine3] varchar(40),
  [CustomerDescriptionLine4] varchar(40),
  [ValidFrom] datetime NOT NULL,
  [StatementDateTime] datetime,
  [StatementVsValidFrom_difference] int,
  PRIMARY KEY ([CustomerAccountNumber])
)
GO

CREATE TABLE [VWCrm_CashBalance_Book] (
  [CustomerAccountNumber] varchar(14) NOT NULL,
  [EndingAccountBalance] money NOT NULL,
  [BalanceValidFrom] datetime NOT NULL,
  PRIMARY KEY ([CustomerAccountNumber])
)
GO

CREATE TABLE [VWCrm_AccountMaster_UDF] (
  [CustomerAccountNumber_Key] char(14) NOT NULL,
  [DistPlan_ExpireDate] datetime,
  [Temporary_CourtOrder_ExpireDate] datetime,
  [BirthCert_OnFile] varchar(4),
  [Age_Of_Majority] datetime,
  [Long_Name_Line_5] varchar(40),
  [Pending_SocialServices_Assessment] varchar(4),
  [Managed_Agency_Code] varchar(4),
  [Managed_Agency_Name] varchar(40),
  [Non_Responsive_Guardian] varchar(4),
  [ValidFrom] datetime NOT NULL,
  PRIMARY KEY ([CustomerAccountNumber_Key])
)
GO

CREATE TABLE [Vcrm_RegionAgencyTribe] (
  [CustomerAccountNumber_Key] char(14) NOT NULL,
  [Agency_Code] varchar(4) NOT NULL,
  [AgencyName] varchar(40) NOT NULL,
  [Region_Code] varchar(4) NOT NULL,
  [RegionName] varchar(40) NOT NULL,
  [Tribe_Code] varchar(4) NOT NULL,
  [TribeName] varchar(40) NOT NULL,
  [StartTime] datetime NOT NULL,
  PRIMARY KEY ([CustomerAccountNumber_Key])
)
GO

CREATE TABLE [VWCrm_Disbursement] (
  [TransactionNumber] char(11) NOT NULL,
  [TransactionCode] char(8) NOT NULL,
  [DisbursementText] varchar(14),
  [CustomerAccountNumber] char(14) NOT NULL,
  [DebitCreditIndicator] char(1) NOT NULL,
  [Amount] money NOT NULL,
  [SettleDate] datetime NOT NULL,
  [Status] char(4),
  [SettledFlag] smallint NOT NULL,
  [PrincIncomeIndicator] char(1) NOT NULL,
  [TaxCode] char(3),
  [TaxYear] char(4),
  [EffectiveDate] datetime,
  PRIMARY KEY ([TransactionNumber])
)
GO
