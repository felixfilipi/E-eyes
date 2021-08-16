SELECT 
    UserPhoto.PhotoDir, 
    UserPhoto.PhotoName,
    UserData.FirstName, 
    UserData.LastName,
    UserData.Gender,
    UserData.Age,
    UserData.Address,
    UserData.Role,
    UserData.LastScan
FROM 
    UserData,
    UserPhoto,
    UserDataset
WHERE
    UserDataset.UserId = UserData.UserId AND
    UserDataset.PhotoId = UserPhoto.PhotoId
GROUP BY
    UserData.FirstName;
