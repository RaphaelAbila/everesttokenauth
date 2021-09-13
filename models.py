from app import db


class Usersauth(db.Model):
    __tablename__ = "usersauth"

    id = db.Column('id',db.Integer, primary_key=True,autoincrement=False)
    email = db.Column('email',db.String(255), nullable=False)
    password_salt = db.Column('password_salt',db.String(255), nullable=False)
    password_hash = db.Column('password_hash',db.String(255), nullable=False)

    def __init__(self,id, email, password_salt, password_hash):
        self.id = id
        self.email = email
        self.password_hash = password_hash
        self.password_salt = password_salt



class Users(db.Model):
    __bind_key__ = 'grader'
    __tablename__ = 'users'
    id = db.Column('id', db.Integer, primary_key=True)
    name= db.Column('name',db.String(255))
    nationality = db.Column('nationality',db.String(255))
    email = db.Column('email',db.String(255))
    registration = db.Column('registration',db.String(255))
    contact = db.Column('contact',db.String(255))
    role = db.Column('role',db.String(255))
    status = db.Column('status',db.Integer)
    school_id = db.Column('school_id',db.BigInteger)
    program = db.Column('program',db.String(255))
    dob = db.Column('dob',db.String(255))
    course = db.Column('course',db.Integer)
    year = db.Column('year',db.Integer)
    month = db.Column('month',db.String(255))
    email_verified_at = db.Column('email_verified_at',db.DateTime)
    password = db.Column('password',db.String(255))
    remember_token = db.Column('remember_token',db.String(100))
    flutter_api= db.Column('flutter_api',db.String(255)) 
    created_at= db.Column('created_at',db.DateTime) 
    updated_at = db.Column('updated_at',db.DateTime)

# class Classes(db.Model):

class Eglesson_attendance(db.Model):
    __bind_key__ = 'campus'
    __tablename__ = 'EGlesson_attendance'
    attendance_id = db.Column('attendance_id',db.Integer, primary_key=True)
    learner_id = db.Column('learner_id',db.Integer)
    class_id = db.Column('class_id',db.Integer)
    exercise_score = db.Column('exercise_score',db.String(30))
    tutor_remark = db.Column('tutor_remark',db.String(1000))
    session_id = db.Column('session_id',db.Integer)
    attendance_code = db.Column('attendance_code',db.String(8))
    tutor_rating = db.Column('tutor_rating',db.Integer)
    registration_number = db.Column('registration_number',db.String(255))
    attendance_confirmed = db.Column('attendance_confirmed',db.String(4))


class Egclasses(db.Model):
    __bind_key__ = 'campus'
    __tablename__ = 'EGclasses' 
    class_id  = db.Column('class_id',db.Integer, primary_key=True)
    subject_id  = db.Column('subject_id',db.Integer)
    year_of_study  = db.Column('year_of_study',db.Integer)
    semester_of_study  = db.Column('semester_of_study',db.Integer)
    start_date  = db.Column('start_date',db.DateTime)
    end_date  = db.Column('end_date',db.DateTime)
    date_created  = db.Column('date_created',db.DateTime)
    intake  = db.Column('intake',db.Integer)


class Eglearners(db.Model):
    __bind_key__ = 'campus'
    __tablename__ = 'EGlearners'
    learner_id  = db.Column('learner_id',db.Integer, primary_key=True)
    first_name  = db.Column('first_name',db.String(30))
    last_name  = db.Column('last_name',db.String(30))
    parent_id  = db.Column('parent_id',db.Integer)
    password  = db.Column('password',db.String(100))
    email  = db.Column('email',db.String(100))
    registration_number  = db.Column('registration_number',db.String(100))


class Egsessions(db.Model):
    __bind_key__ = 'campus'
    __tablename__ = 'EGsessions'
    session_id  = db.Column('session_id',db.Integer, primary_key=True)
    learner_id  = db.Column('learner_id',db.Integer)
    tutor_id  = db.Column('tutor_id',db.Integer)
    subject_id  = db.Column('subject_id',db.Integer)
    session_day  = db.Column('session_day',db.String(9))
    start_month  = db.Column('start_month',db.String(15))
    date_created  = db.Column('date_created',db.DateTime)
    session_dates  = db.Column('session_dates',db.DateTime)
    expected_duration  = db.Column('expected_duration',db.Float)
    actual_duration  = db.Column('actual_duration',db.Float)
    topic  = db.Column('topic',db.String(50))
    sub_topic  = db.Column('sub_topic',db.String(150))
    tutor_remark  = db.Column('tutor_remark',db.String())
    offline_resources  = db.Column('offline_resources',db.String(1000))
    online_resources  = db.Column('online_resources',db.String(1000))
    exercise_score  = db.Column('exercise_score',db.String(30))
    test_score  = db.Column('test_score',db.String(30))
    exercise_file  = db.Column('exercise_file',db.String(50))
    learner_remark  = db.Column('learner_remark',db.String(1000))
    billing_type  = db.Column('billing_type',db.String(8))
    tutor_rate  = db.Column('tutor_rate',db.Integer)
    parent_rate  = db.Column('parent_rate',db.Integer)
    tutor_expected_income  = db.Column('tutor_expected_income',db.Integer)
    parent_expected_bill  = db.Column('parent_expected_bill',db.Integer)
    tutor_actual_income  = db.Column('tutor_actual_income',db.Integer)
    parent_actual_bill  = db.Column('parent_actual_bill',db.Integer)
    parent_id  = db.Column('parent_id',db.Integer)
    parent_comment  = db.Column('parent_comment',db.String(1000))
    completed_session = db.Column('completed_session',db.Integer)
    tutor_created_session = db.Column('tutor_created_session',db.Integer)
    locked = db.Column('locked',db.String(8))
    transfered_to = db.Column('transfered_to',db.Integer)
    transfered_from = db.Column('transfered_from',db.Integer)
    class_id = db.Column('class_id',db.Integer)



class Egsubjects(db.Model):
    __bind_key__ = 'campus'
    __tablename__ = 'EGsubjects'
    subject_id = db.Column('subject_id',db.Integer, primary_key=True)
    subject_name = db.Column('subject_name',db.String(100))
    subject_code = db.Column('subject_code',db.String(100))
    subject_curriculum = db.Column('subject_curriculum',db.Integer)    

class Student_class_allocation(db.Model):
    __bind_key__ = 'campus'
    __tablename__ = 'student_class_allocation'
    allocation_id = db.Column('allocation_id',db.Integer, primary_key=True)
    class_id = db.Column('class_id',db.Integer)
    learner_id = db.Column('learner_id',db.Integer)
    date_created = db.Column('date_created',db.DateTime)