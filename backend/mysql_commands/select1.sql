SELECT
    UserScanPhoto.PhotoDir,
    UserScanPhoto.PhotoName,
    UserScan.FirstName,
    UserScan.LastName,
    UserScan.Gender,
    UserScan.Age,
    UserScan.Address,
    UserScan.Role,
    UserScan.ScanDate
FROM
    UserScan,
    UserScanPhoto
WHERE
    UserScan.UserId = UserScanPhoto.UserId;
