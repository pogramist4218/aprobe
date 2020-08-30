import uuid
import route as r
import validate as vld
import voicer as v
import file_loger as fl
import database_loger as db

FILE_LOG = int(1)
DB_LOG   = int()

PHONE = str()
PATH  = str()
STAGE = str()

if __name__ == "__main__":
    arguments = r.runRouting()

    if vld.validate(arguments):
        PHONE   = arguments.phone
        DB_LOG  = arguments.database
        PATH    = arguments.path
        STAGE   = arguments.stage

        message = v.readingSound(PATH)
        status, response, duration = v.analyseMessage(message, STAGE)
        logMessage = {
            'uid':      str(uuid.uuid4()),
            'stage':    'stage №' + str(STAGE),
            'phone':    PHONE,
            'duration': duration,
            'status':   status
        }
        fl.logInfo("{uid} - {stage} - {phone} - {duration} - {status}".format(**logMessage))
        if(DB_LOG == 1):
            db.logInfo(logMessage)
        r.removeFileByPath(PATH)
