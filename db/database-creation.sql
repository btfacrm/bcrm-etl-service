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
  [ContactName] varchar(80),
  [DateOfBirth] datetime,
  [DateOfDeath] datetime,
  [ActiveFlag] smallint,
  [PrimaryLastName] varchar(20),
  [PrimaryFirstName] varchar(12),
  [PrimaryMiddleInitial] varchar(20),
  [PrimaryGender] varchar(4),
  [DisbursementEligibilityFlag] smallint,
  [ValidFrom] datetime,
  PRIMARY KEY ([ContactID])
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
