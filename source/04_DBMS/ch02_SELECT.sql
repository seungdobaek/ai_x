-- [II] SELECT문 - 조회
SELECT * FROM TAB; -- 현재 계정 (SCOTT)

-- 1. SELECT 문장 작성법
SELECT * FROM TAB; -- 현 계정이 가지고 있는 테이블 정보(실행 : CTRL+ENTER)
SELECT * FROM DEPT; -- DEPT 테이블의 모든 열 모든 행
SELECT * FROM SALGRADE; -- SALGRADE 테이블의 모든 열, 모든 행
SELECT * FROM EMP; -- EMP 테이블의 모든 열, 모든 행

-- 2. 특정 열만 출력
DESC EMP;
    -- EMPT 테이블의 구조
SELECT EMPNO, ENAME, SAL, JOB FROM EMP; --EMP 테이블의 SELECT절에 지정된 열만 출력
SELECT EMPNO AS "사 번", ENAME AS "이 름", SAL AS "급여", JOB AS "직책" FROM EMP;
    -- 열이름에 별칭을 두는 경우 EX. 열이름 AS 별칭
SELECT EMPNO "사 번", ENAME "이 름", SAL "급여", JOB "직책" FROM EMP;
    -- AS 생략가능 : 열이름에 별칭을 두는 경우 EX. 열이름 별칭, 열이름 별칭
SELECT EMPNO "사 번", ENAME "이 름", SAL 급여, JOB FROM EMP;
    -- AS 생략가능, 별칭에 SPACE가 없을경우 따옴표 생략 가능
    
-- 3. 특정 행 출력 : WHERE(조건절) -- 비교 연산자 :  >, >=, <, <=, 다르다(!=, ^=, <>), 같다(=)
SELECT EMPNO 사번, ENAME 이름, SAL 급여 FROM EMP WHERE SAL=3000;
SELECT EMPNO NO, ENAME NAME, SAL FROM EMP WHERE SAL!=3000;
SELECT EMPNO NO, ENAME NAME, SAL FROM EMP WHERE SAL^=3000;
SELECT EMPNO NO, ENAME NAME, SAL FROM EMP WHERE SAL<>3000;
    -- 비교영ㄴ산자는 숫자, 문자, 날짜형 모두 가능
    -- EX1. 사원이름이 'A', 'B', 'C'로 시작하는 사원의 모든 열
    -- A < AA < AAA < .... < B < BA < .... < C
SELECT * FROM EMP WHERE ENAME < 'D';
    -- EX2. 81년도 이전에 입사한 사원의 모든 열 (필드)
SELECT * FROM EMP WHERE HIREDATE < '81/01/01';
    -- EX3. 부서 번호가 10번인 사원의 모든 필드
SELECT * FROM EMP WHERE DEPTNO=10;
    -- SQL문은 대소문자 구별없음. 데이터는 대소문자 구별
    -- EX4. 이름이 SCOTT인 직원의 모든 데이터
SELECT * FROM EMP WHERE ENAME='SCOTT';

-- 4. WHERE절(조건절)에 논리연산자 : AND, OR, NOT
    -- EX1. 급여가 2000이상 3000이하인 직원의 모든 필드
SELECT * FROM EMP WHERE SAL >= 2000 AND SAL <= 3000;
    -- EX2. 82년도 입사한 사원의 모든 필드
SELECT * FROM EMP WHERE HIREDATE<'83/01/01' AND HIREDATE>='82/01/01';
    -- 날짜 표기법 세팅 (현재:RR/MM/DD)
ALTER SESSION SET NLS_DATE_FORMAT = 'RR-MM-DD';
SELECT * FROM EMP
    WHERE TO_CHAR(HIREDATE, 'RR/MM/DD') < '83/01/01' 
        AND TO_CHAR(HIREDATE, 'RR/MM/DD') >= '82/01/01';
    -- EX3. 부서 번호가 10이 아닌 직원의 모든 필드
SELECT * FROM EMP WHERE DEPTNO != 10;
SELECT * FROM EMP WHERE NOT DEPTNO = 10;

-- 5. 산술연산자 (SELECT절, WHERE절, ORDER BY절)
SELECT EMPNO, ENAME, SAL "예전월급", SAL*1.1 "현재월급" FROM EMP;
    -- EX1. 연봉이 10000이상인 직원의 ENAME(이름), SAL(월급), 연봉
SELECT ENAME, SAL, SAL*12 ANNSAL    --ORACLE에서 읽는 순서 (3)
    FROM EMP                        -- (1)
    WHERE SAL*12 >= 10000           -- (2)
    ORDER BY ANNSAL;                -- (4)
    -- EX2. 연봉이 20000 이상인 직원의 이름, 월급, 상여, 연봉 출력
    -- 산술 연산의 결과는 NULL을 포함하면 결과도 NULL
    -- NVL(NULL 일수도 있는 필드명, 대체값)을 이용 : 필드명과 대체값은 타입이 일치
SELECT ENAME, SAL, COMM, SAL*12+NVL(COMM,0) 연봉 FROM EMP WHERE SAL*12+NVL(COMM,0) >= 20000;
    -- EX3. 모든 사원의 ENAME, MGR(상사사번)을 출력, 단 상사사번이 없으면 'CEO'
SELECT ENAME, NVL(TO_CHAR(MGR),'CEO') MGR FROM EMP;

-- 6. 연결연산자 (||) : 필드내용이나 문자를 연결
SELECT ENAME ||'은(는)'|| JOB FROM EMP;

-- 7. 중복제거(DISTINCT)
SELECT DISTINCT JOB FROM EMP;
SELECT DISTINCT DEPTNO FROM EMP;

-- 연습문제
--1. emp 테이블의 구조 출력
DESC EMP;
--2. emp 테이블의 모든 내용을 출력 
SELECT * FROM EMP;
--3. 현 scott 계정에서 사용가능한 테이블 출력
SELECT * FROM TAB;
--4. emp 테이블에서 사번, 이름, 급여, 업무, 입사일 출력
SELECT EMPNO 사번, ENAME 이름, SAL 급여, JOB 업무, HIREDATE 입사일 FROM EMP;
--5. emp 테이블에서 급여가 2000미만인 사람의 사번, 이름, 급여 출력
SELECT EMPNO 사번, ENAME 이름, SAL 급여 FROM EMP WHERE SAL<2000;
--6. 입사일이 81/02이후에 입사한 사람의 사번, 이름, 업무, 입사일 출력
SELECT EMPNO 사번, ENAME 이름, JOB 업무, HIREDATE 입사일 FROM EMP WHERE TO_CHAR(HIREDATE, 'RR/MM/DD') > '82/02/01';
--7. 업무가 SALESMAN인 사람들 모든 자료 출력
SELECT * FROM EMP WHERE JOB = 'SALESMAN';
--8. 업무가 CLERK이 아닌 사람들 모든 자료 출력
SELECT * FROM EMP WHERE JOB != 'CLERK';
--9. 급여가 1500이상이고 3000이하인 사람의 사번, 이름, 급여 출력
SELECT EMPNO 사번, ENAME 이름, SAL 급여 FROM EMP WHERE SAL >=1500 AND SAL<=3000;
--10. 부서코드가 10번이거나 30인 사람의 사번, 이름, 업무, 부서코드 출력
SELECT EMPNO 사번, ENAME 이름, JOB 업무, DEPTNO 부서코드 FROM EMP WHERE DEPTNO=10 OR DEPTNO=30;
--11. 업무가 SALESMAN이거나 급여가 3000이상인 사람의 사번, 이름, 업무, 부서코드 출력
SELECT EMPNO 사번, ENAME 이름, JOB 업무, DEPTNO 부서코드 FROM EMP WHERE JOB='SALESMAN' OR SAL>=3000;
--12. 급여가 2500이상이고 업무가 MANAGER인 사람의 사번, 이름, 업무, 급여 출력
SELECT EMPNO 사번, ENAME 이름, JOB 업무, SAL 급여 FROM EMP WHERE SAL>=2500 AND JOB='MANAGER';
--13.“ename은 XXX 업무이고 연봉은 XX다” 스타일로 모두 출력(연봉은 SAL*12+COMM)
SELECT ENAME || '은' || JOB || ' 업무이고 연봉은 '|| (SAL*12+NVL(COMM,0)) || '다' 상세설명 FROM EMP;

-- 8. SQL연산자 (BETWEEN, IN, LIKE, IS NULL)
-- (1) BETWEEN A AND B : A부터 B까지 (A, B 포함. A<=B)
    -- EX1. SAL이 1500 이상 3000 이하
SELECT * FROM EMP WHERE SAL>=1500 AND SAL<=3000;
SELECT * FROM EMP WHERE SAL BETWEEN 1500 AND 3000;
SELECT * FROM EMP WHERE SAL BETWEEN 3000 AND 1500; -- X 이거는 안됨 항상 작은게 앞으로
-- EX1-1. SAL이 1500 미만 3000초과 (EX1의 반대)
SELECT * FROM EMP WHERE SAL NOT BETWEEN 3000 AND 1500;
SELECT * FROM EMP WHERE SAL<1500 OR SAL>3000;
--EX2. 81년도 봄(3월~5월)에 입사한 직원의 모든 필드
SELECT * FROM EMP WHERE TO_CHAR(HIREDATE,'RR/MM/DD') BETWEEN '81/03/01' AND '81/05/31';
-- (2) 필드명 IN (값1, 값2, ...., 값N)
    -- EX1. 부서코드가 10번이거나 30인 사람의 모든 정보
SELECT * FROM EMP WHERE DEPTNO IN (10,30);
    -- EX2. 직책(JOB)이 'MANAGER'이거나 'ANALYST'인 사원의 모든 정보
SELECT * FROM EMP WHERE JOB IN ('MANAGER', 'ANALYST');
    -- EX1-1. EX1의 반대( 부서코드가 10번이거나 30이 아닌 사람의 모든 정보
SELECT * FROM EMP WHERE DEPTNO NOT IN (10,30);
-- (3) LIKE 필드명 LIKE '패턴' : %(0글자이상), _(하나의 문자 아무거나)를 포함하는 패턴)
    -- EX1. 이름이 M으로 시작하는 사원의 모든 정보
SELECT * FROM EMP WHERE ENAME LIKE 'M%';
    -- EX2. 이름이 S로 끝나는 사원의 모든 정보
SELECT * FROM EMP WHERE ENAME LIKE '%S';
    -- EX3. 이름에 N이 들어가는 사원의 모든 정보
SELECT * FROM EMP WHERE ENAME LIKE '%N%';
    -- EX4. 이름에 N이 들어가고 JOB에 S가 들어가는 사원의 모든정보
SELECT * FROM EMP WHERE ENAME LIKE '%N%' AND JOB LIKE '%S%';
    -- EX5. SAL이 5로 끝나는 사원 모든 정보
SELECT * FROM EMP WHERE SAL LIKE '%5';
    -- EX6. 입사일이 82년도에 입사한 사원
SELECT * FROM EMP WHERE TO_CHAR(HIREDATE, 'RR/MM/DD') LIKE '82/%'; --'82/__/__도 가능'
SELECT * FROM EMP WHERE TO_CHAR(HIREDATE, 'RR')=82;
    -- EX7. 1월에 입사한 사원
SELECT * FROM EMP WHERE TO_CHAR(HIREDATE, 'RR/MM/DD') LIKE '__/01/__';
SELECT * FROM EMP WHERE TO_CHAR(HIREDATE, 'MM')=01;
    -- EX8. 이름에 %가 등러간 사원
SELECT * FROM EMP WHERE ENAME LIKE '%\%%' ESCAPE '\';
    --INSERT INTO EMP VALUES (9999, '홍%동', NULL, NULL, NULL, 9000, 9000, 40);-- 이름에 %들어간 데이터 INERT
SELECT * FROM EMP;
ROLLBACK; -- DML(데이터조작어; 추가, 수정, 삭제, 검색)을 취소

-- (4) 필드명 IS NULL : 필드명이 널인지를 검색할때
    --EX1. COMM(상여금)이 없는 사원
SELECT * FROM EMP WHERE COMM IS NULL OR COMM=0;
    --EX2. 상여금을 받는 사원
SELECT * FROM EMP WHERE COMM!=0;

-- 9. 정렬(오름차순, 내림차순) : ORDER BY 절
SELECT * FROM EMP ORDER BY SAL;
SELECT * FROM EMP ORDER BY SAL DESC;
    -- EX1. 급여 내림차순, 급여같으면 입사일이 내림차순
SELECT * FROM EMP ORDER BY SAL DESC, HIREDATE DESC;
    -- EX2. 급여 2000 초과 사원을 이름 abc순
SELECT * FROM EMP WHERE SAL>2000 ORDER BY ENAME;

-- 총 연습문제
--1.	EMP 테이블에서 sal이 3000이상인 사원의 empno, ename, job, sal을 출력
 SELECT EMPNO, ENAME, JOB, SAL FROM EMP WHERE SAL>=3000;
--2.	EMP 테이블에서 empno가 7788인 사원의 ename과 deptno를 출력
SELECT ENAME, DEPTNO FROM EMP WHERE EMPNO=7788;
--3.	연봉(SAL*12+COMM)이 24000이상인 사번, 이름, 급여 출력 (급여순정렬)
SELECT EMPNO, ENAME, SAL FROM EMP WHERE SAL*12+NVL(COMM,0) >= 24000
    ORDER BY SAL;
--4.	입사일이 1981년 2월 20과 1981년 5월 1일 사이에 입사한 사원의 사원명, 직책, 입사일을 출력 (단 hiredate 순으로 출력)
SELECT ENAME, JOB, HIREDATE FROM EMP 
    WHERE TO_CHAR(HIREDATE,'RR/MM/DD') BETWEEN '81/02/20' AND '81/05/01'
    ORDER BY HIREDATE;
--5.	deptno가 10,20인 사원의 모든 정보를 출력 (단 ename순으로 정렬)
SELECT * FROM EMP WHERE DEPTNO IN (10,20) ORDER BY ENAME;
--6.	sal이 1500이상이고 deptno가 10,30인 사원의 ename과 sal를 출력
-- (단 출력되는 결과의 타이틀을 employee과 Monthly Salary로 출력)
SELECT ENAME "employee", SAL "Monthly Salary" FROM EMP
    WHERE SAL>=1500 AND DEPTNO IN (10,30);
--7.	hiredate가 1982년인 사원의 모든 정보를 출력
SELECT * FROM EMP WHERE TO_CHAR(HIREDATE, 'RR')=82;
--8.	이름의 첫자가 C부터  P로 시작하는 사람의 이름, 급여 이름순 정렬
SELECT ENAME, SAL FROM EMP WHERE ENAME>='C' AND ENAME<'Q'
    ORDER BY ENAME;
--9.	comm이 sal보다 10%가 많은 모든 사원에 대하여 이름, 급여, 상여금을 
--출력하는 SELECT 문을 작성
SELECT ENAME, SAL, COMM FROM EMP WHERE COMM>SAL*1.1;
--10.	job이 CLERK이거나 ANALYST이고 sal이 1000,3000,5000이 아닌 모든 사원의 정보를 출력
SELECT * FROM EMP WHERE JOB IN ('CLERK', 'ANALYST') AND SAL NOT IN (1000, 3000, 5000);
--11.	ename에 L이 두 자가 있고 deptno가 30이거나 또는 mgr이 7782인 사원의 
--모든 정보를 출력하는 SELECT 문을 작성하여라.
SELECT * FROM EMP WHERE ENAME LIKE '%L%L%' AND (DEPTNO=30 OR MGR=7782);

--12.	입사일이 81년도인 직원의 사번, 사원명, 입사일, 업무, 급여를 출력
SELECT EMPNO, ENAME, HIREDATE, JOB, SAL FROM EMP
    WHERE TO_CHAR(HIREDATE,'RR')=81;
--13.	입사일이81년이고 업무가 'SALESMAN'이 아닌 직원의 사번, 사원명, 입사일, 
-- 업무, 급여를 검색하시오.
SELECT EMPNO, ENAME, HIREDATE, JOB, SAL FROM EMP
    WHERE TO_CHAR(HIREDATE,'RR')=81 AND NOT JOB='SALESMAN';
--14.	사번, 사원명, 입사일, 업무, 급여를 급여가 높은 순으로 정렬하고, 
-- 급여가 같으면 입사일이 빠른 사원으로 정렬하시오.
SELECT EMPNO, ENAME, HIREDATE, JOB, SAL FROM EMP
    ORDER BY SAL DESC, HIREDATE;
--15.	사원명의 세 번째 알파벳이 'N'인 사원의 사번, 사원명을 검색하시오
SELECT EMPNO, ENAME FROM EMP WHERE ENAME LIKE '__N%';
--16.	사원명에 'A'가 들어간 사원의 사번, 사원명을 출력
SELECT EMPNO, ENAME FROM EMP WHERE ENAME LIKE '%A%';
--17.	연봉(SAL*12)이 35000 이상인 사번, 사원명, 연봉을 검색 하시오.
SELECT EMPNO, ENAME, SAL*12 ANNSAL FROM EMP WHERE SAL*12>=35000;