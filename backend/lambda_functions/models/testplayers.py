from players import *
from storage import *
CREDS = {
  "type": "service_account",
  "project_id": "pingpong-388022",
  "private_key_id": "0518786463a09baf93163f3afd803272090a4f1e",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC47H7jJKGinTcS\ntKTweQ0mcuwdezdAHBVYvRQV6CqwFg/QlZypdzmDHIP1VcL1chS2/yEqZAHQg4hR\nNjZrBlaAJkMAVNlDphqAmst2aY0cebaVgxXqiHKXkfrHTU/PLDkmDNXAgxDrxoF/\nOZ6py6shr1tbeXIJLtg8BFRsQyl9wIPdEL29GeoltgzNaA6BTqQxQ+PaIE1wRo4g\nMQyge9DLe8vsg8bLc2RmkHJaiLvkAvpd9VvAOwg2gpD0SclbPDQdfwM+x3bXoSlB\nTgt4kLqRAhmEEYEmSqrMirXMv9o/hyGhH/6IQJownjotu7jAHHdgO8W2JcJIduqA\n8uXX02CFAgMBAAECggEACXNDNsNtTodJ7wxJQ5AZcnC8DUj54AOvZEC2u+SIo0Vg\nBdund7zuilCU6R7lXtq3dp9KKBrtQXp/UbsmA8kn9tY9uqYbZkrLnu003vZyQ4Aa\n1cAvCLR0EA03QM58I3e8l0EKVBNpSXX0XIvqxlLwtMDRN+GtyLdaoz02EpmfZLGG\nrP9PuTISOi6fXd3KRBfxMwmw4RbqLsx75NC1pC9PQmmG2uteqIOrEbx1Ke557RFd\nZ5No8OOloi9fHr+Js+WL8unCvVK1GZcnROQeNmd6mBLHmA9BwIMWa1xD3VgdHmqH\noAY+QZxfxQE1ZRZoNKRS6lgeuX/+9DVjLsk42vsOjwKBgQD2cvAlqM8dfA4tLgc9\nJdDWF7wysCV/gmftqcU8tiG3OXWb+e8IfDMU4vhTFL5C6znqCbDorCty47C7RK/W\n/tXJJSYBeQbqwl+L/WtSlS3P63uWJjbNMTK8XwZdQa3/AkeMitvYAEn04B5A2d8A\nBb79ytVqs8t1AIb/QpFINpsFwwKBgQDAFyfwy+jM7HKX3+eKXn6pZhcLCElpZfb7\nk/gGupHj7tW+eygYWTBD4+PT7VE0GUl+H2Mf+zZPQaV9nxd1vEvueF0PJHytVfdd\n2DhZYOtejybdcnPlnu+T8XVfXP4gMiDQODOX3ClYZxaz1ia9t9coe+FCxP7I8LjX\neLJ86Xj0FwKBgEz+zc5GNib1CgzNc4+EEAHDOpXveFek60lSH//+uvveZMMNS8Ov\n4dmlq4VxVpvbl6Vpz65xk8V6I03ugK0/wpTsGTqekC2p+mXnD6+mUcDCxkK7v6VN\nuJcnbPqXuX+RO79J5rNOK8zodCs4pjYAlZH+27xRXcA5IPQA3RjdjoM3AoGBAJiB\nyfQj8HDCSTjLS8lPvMBBjYn0ylQj4DNdB05QUgPlW04f+XVbWjaMeBWKFS6H5RF9\nWfXKPRQvynQyGy4ekSqD5V5gWZxE5GBdil9r03L/tJucgueLiCqtScKs0hY9tk+a\nT1wCL9FAB4ZAQAHgM7Kwp+ea/64JcLeh3BPQSXeBAoGAD/QJSx6o3/xZJjlj/eln\ni3Lb/8GSS/sFQCDsPN6ikGZF4Ci+85T6+kgPgIqRpw9i3Uvj2c5Xi8eoOkfyrv86\nec89bGHJoRKhSZn+W+vHgM0Z10tVOpwHXf64ICIXP5xALgZnMaiKoHRqA8p1bdpy\nbDH5WCCaco5TjzIJEtFGit4=\n-----END PRIVATE KEY-----\n",
  "client_email": "pingpong-service-account@pingpong-388022.iam.gserviceaccount.com",
  "client_id": "105954252746091336431",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/pingpong-service-account%40pingpong-388022.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}

SHEET_KEY = "15Y_utiGGYxutHQixJHefDa0JiTu6kB5PZY90Uu0o9iQ"

spreadsheet = get_spreadsheet(CREDS, SHEET_KEY)
sheet = get_sheet(spreadsheet, 1)

players = Players(sheet)

#players.addPlayer('Alice')
#players.addPlayer('Bob')
#players.addPlayer('David')
#players.addPlayer('TEST')
#players.removePlayer('test')

players.addPointandMarkLoss('Alice', 'Bob')
players.addPointandMarkLoss('David', 'Alice')
players.addPointandMarkLoss('David', 'Alice')
