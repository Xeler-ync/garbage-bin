/*
coding = utf-8
Naming convention:
    global variable ->  upper camel case
    function        ->  lower camel case
    local variable  ->  under score case
Author: Xeler
Platform: x86-64
*/

#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>


#define MAX_STUDENTS 111

enum ExtraBool
{
    Unset, False, True
};
enum GPA
{
    Unset1, Ap, A, Bp, B, Cp, C, D, F
};
enum ReadyFor
{
    UnReady, Id, Score, Rank
};


struct Student
{
    char fname[20];
    char lname[20];
    int score;
    long long int id;
    enum GPA GPA;
    int rank;
    enum ExtraBool rebuild;
};

static struct Student Data[MAX_STUDENTS];
static struct Student DataCache[MAX_STUDENTS];
int DataCount = 0;
int OperateInput = 0;
void *freeer = NULL;
enum ExtraBool DataReadyForRank = False;
enum ReadyFor DataReady = UnReady; // Never equals Rank
enum ReadyFor DataCacheReady = UnReady;
enum ExtraBool AlwaysTrySaveSource = True;
enum ExtraBool AlwaysTryBinarySearch = True;
enum ExtraBool AlwaysRecalculateBeforeOutput = True;
enum ExtraBool AlwaysCalculateAllRanksWhenWorkingOnData = True;

void appendStudent(int n);
void calcGPA(int index);
void calcAllGPA();
void deleteStudent(long long int id);
int searchStudentById(long long int id);
void sortDataById();
void getSortedDataById(enum ReadyFor *ready_state, struct Student *tgt);
void sortDataByScore(struct Student *tgt, int n);
void getSortedDataByScore(enum ReadyFor *ready_state, struct Student *tgt);
void printStudent(int index);
int findMax();
int findMin();
int calcAvg();
enum ExtraBool prime(long long int id);
enum ExtraBool coprime(long long int id1, long long int id2);
char* encrypt(int key);
char* decrypt(int key, char *str);
char* multi(int m);
void quickSort(int *arr, int lower, int upper);
void shellSort(int *arr, int n);
int cmpId(const void *a,const void *b);
int cmpScore(const void *a,const void *b);
int binarySearchId(long long int id, int lower, int upper);
int linearSearchId(long long int id, int lower, int upper);
void calcRankToCache();
int calcRank(enum ExtraBool const_Data, int index_from_Data);
void calcAllRank();
void setSettings();
void optMenu(int type);
void reflashOperateInput();
void selectCase();

// Syntactic sugars
void Add(char *name, int id, int score);
void Adds(int n, char name[], int id[], int score[]);
void Delete(long long int id);
void Search(long long int id);
void Sort_by_id();
void Sort_by_score();
int Max();
int Min();
int Ave();

void appendStudent(int n){
    if (n + DataCount > MAX_STUDENTS)
    {
        printf(
            "too much data! %d + %d > %d",
            n,
            DataCount,
            MAX_STUDENTS
            );
        return;
    }
    enum ExtraBool direct = False;
    struct Student *tgt = NULL;
    int fixed_n = n;

    // switch Ready state below
    DataCacheReady = UnReady;
    // if is unsorted or Data is empty
    if ((Id == DataReady && Score == DataReady) || 0 == DataCount)
    {
        tgt = Data + DataCount;
        direct = True;
        fixed_n = 0;
        if (0 == DataCount)
        {
            DataReady = UnReady;
        }
    }
    else
    {
        DataReady = UnReady;
    }

    if (False == direct)
    {
        tgt = DataCache;
    }

    for (size_t i = 0; i < n; ++i)
    {
        scanf(
            "%s %s %lld %d",
            &((tgt+i)->fname),
            &((tgt+i)->lname),
            &((tgt+i)->id),
            &((tgt+i)->score)
            );
        ++DataCount;
    }

    if (True == direct)
    {
        // do nothing
    }
    else
    {
        int (*cmper)(const void *,const void *) = NULL;
        if (Id == DataReady)
        {
            cmper = cmpId;
        }
        else if (Score == DataReady)
        {
            cmper = cmpScore;
        }

        qsort(tgt,n,sizeof(struct Student),cmper);
        int main_index = DataCount -1, rest_n = n, cmping_data_index = main_index - n;
        for (int i = n - 1 + 1; i > 0; --i)
        {
            for (int j = cmping_data_index; j >= 0; --j)
            {
                if (1 == cmper(&Data[j],&tgt[i-1]))
                {
                    Data[j+rest_n] = Data[j];
                    --cmping_data_index;
                    if (-1 == cmping_data_index)
                    {
                        for (size_t k = 0; k < rest_n; ++k)
                        {
                            Data[k] = tgt[k];
                        }
                    }
                }
                else // -1
                {
                    Data[j+rest_n] = tgt[i-1];
                    --rest_n;
                    break;
                }
            }
        }
    }
}

void calcGPA(int index){
    Data[index].rebuild = False;
    if (Data[index].score >= 93)
    {
        Data[index].GPA = Ap;
    }
    else if (Data[index].score >= 85)
    {
        Data[index].GPA = A;
    }
    else if (Data[index].score >= 80)
    {
        Data[index].GPA = Bp;
    }
    else if (Data[index].score >= 75)
    {
        Data[index].GPA = B;
    }
    else if (Data[index].score >= 70)
    {
        Data[index].GPA = Cp;
    }
    else if (Data[index].score >= 65)
    {
        Data[index].GPA = C;
    }
    else if (Data[index].score >= 60)
    {
        Data[index].GPA = D;
    }
    else
    {
        Data[index].GPA = F;
        Data[index].rebuild = True;
    }
}

void calcAllGPA(){
    for (size_t i = 0; i < DataCount; i++)
    {
        calcGPA(i);
    }
}

void deleteStudent(long long int id){
    int index = searchStudentById(id);
    for (; index < DataCount; ++index)
    {
        Data[index] = Data[index+1];
    }
    DataCount --;
    DataCacheReady = UnReady;
}

int searchStudentById(long long int id){
    // Must remember that upper equals index + 1
    if (True == AlwaysTryBinarySearch && Id != DataReady)
    {
        // select target array by AlwaysTrySaveSource
        enum ReadyFor *ready_state = NULL;
        struct Student *tgt = NULL;
        getSortedDataById(ready_state,tgt);
    }
    if (Id == DataReady)
    {
        return binarySearchId(id,0,DataCount);
    }
    else
    {
        return linearSearchId(id,0,DataCount);
    }
}

void sortDataById(struct Student *tgt, int n){
    qsort(tgt,n,sizeof(struct Student),cmpId);
    if (Data == tgt)
    {
        printf("[Data has been sorted by Id]\n");
        DataReady = Id;
        if (Rank == DataCacheReady)
        {
            DataCacheReady = UnReady;
        }
    }
    else if (DataCache == tgt)
    {
        printf("[DataCache has been sorted by Id]\n");
        DataCacheReady = Id;
    }
    else
    {
        printf("[An array has been sorted by Id]\n");
    }
}

void getSortedDataById(enum ReadyFor *ready_state, struct Student *tgt){
    // select target array by AlwaysTrySaveSource
    if (True == AlwaysTrySaveSource)
    {
        // it is useable if Data was sorted by Id
        if (Id == DataReady)
        {
            ready_state = &DataReady;
            tgt = Data;
        }

        ready_state = &DataCacheReady;
        tgt = DataCache;
    }
    else
    {
        ready_state = &DataReady;
        tgt = Data;
    }

    // Data should be ReadyForId
    if (Id != *ready_state)
    {
        sortDataById(tgt,DataCount);
    }
}

void sortDataByScore(struct Student *tgt, int n){
    qsort(tgt,n,sizeof(struct Student),cmpScore);
    if (Data == tgt)
    {
        printf("[Data has been sorted by Score]\n");
        DataReady = Score;
        if (Rank == DataCacheReady)
        {
            DataCacheReady = UnReady;
        }
    }
    else if (DataCache == tgt)
    {
        printf("[DataCache has been sorted by Score]\n");
        DataCacheReady = Score;
    }
    else
    {
        printf("[An array has been sorted by Score]\n");
    }
}

void getSortedDataByScore(enum ReadyFor *ready_state, struct Student *tgt){
    // select target array by AlwaysTrySaveSource
    if (True == AlwaysTrySaveSource)
    {
        // it is useable if Data was sorted by Id
        if (Score == DataReady)
        {
            ready_state = &DataReady;
            tgt = Data;
        }

        ready_state = &DataCacheReady;
        tgt = DataCache;
    }
    else
    {
        ready_state = &DataReady;
        tgt = Data;
    }

    // Data should be ReadyForScore
    if (Score != *ready_state)
    {
        sortDataByScore(tgt,DataCount);
    }
}

void printStudent(int index){
    // I didn't use standerd optput format because I think this format can be easier to read
    if (True == AlwaysRecalculateBeforeOutput)
    {
        calcGPA(index);
    }
    printf(
        "%.12lld %.3d %.2s %.1d %.6s %s %s\n",
        Data[index].id,
        Data[index].score,
        (Ap == Data[index].GPA) ? "A+":
        (A  == Data[index].GPA) ? "A ":
        (Bp == Data[index].GPA) ? "B+":
        (B  == Data[index].GPA) ? "B ":
        (Cp == Data[index].GPA) ? "C+":
        (C  == Data[index].GPA) ? "C ":
        (D  == Data[index].GPA) ? "D ":
        (F  == Data[index].GPA) ? "F ":
        "\b",
        (True == AlwaysRecalculateBeforeOutput) ? calcRank(True, index) :
        (True == DataReadyForRank) ? Data[index].rank :
        '\b',
        (True  == Data[index].rebuild) ? "Unpass" :
        (False == Data[index].rebuild) ? "Passed" :
        "\b",
        Data[index].fname,
        Data[index].lname
    );
}

int findMax(){
    if (Score == DataReady)
    {
        return DataCount;
    }
    int max_index = 0;
    for (size_t i = 0; i < DataCount; ++i)
    {
        max_index = (Data[max_index].score < Data[i].score) ? i : max_index;
    }
    return max_index;
}

int findMin(){
    if (Score == DataReady)
    {
        return 0;
    }
    int min_index = 0;
    for (size_t i = 0; i < DataCount; ++i)
    {
        min_index = (Data[min_index].score > Data[i].score) ? i : min_index;
    }
    return min_index;
}

int calcAvg(){
    long long int sum;
    for (size_t i = 0; i < DataCount; ++i)
    {
        sum += Data[i].score;
    }
    return sum / DataCount;
}

enum ExtraBool prime(long long int id){
    int score = Data[searchStudentById(id)].score;

    /*
    A number can be expressed from 6n to 6n+5, except for 2 and 3, only 6n+1 and 6n+5 can be prime.
    Here is the algorithm implementation.
    Which can be faster I think.
    */
    if (2 == score || 3 == score)
    {
        return True;
    }
    else if (1 == score % 6 || 5 == score % 6 || 1 == score)
    {
        return False;
    }
    else
    {
        for (size_t i = 5; i < sqrt(score) + 6; i += 6)
        {
            if (0 == score % i || 0 == score % (i+2))
            {
                return False;
            }
        }
        return True;
    }
}

enum ExtraBool coprime(long long int id1, long long int id2){
    int score1 = Data[searchStudentById(id1)].score;
    int score2 = Data[searchStudentById(id2)].score;

    // If both of them are odd, they can't be coprime.
    if (0 == score1 & 1 && 0 == score2 & 2)
    {
        return True;
    }

    // Euclidean algorithm here.
    int temp = 114514;
    while (0 != temp)
    {
        temp = score1 % score2;
        score1 = score2;
        score2 = temp;
    }
    return (0 == score1) ? True : False;
}

char* encrypt(int key){
    // allocate heap memory to return
    char* result;
    result = (char *)calloc(DataCount*3*2+1,sizeof(char));

    // select target array by AlwaysTrySaveSource
    enum ReadyFor *ready_state = NULL;
    struct Student *tgt = NULL;
    getSortedDataById(ready_state,tgt);

    int result_index = 0 - 1;
    for (size_t i = 0; i < DataCount; i++)
    {
        int processing_score = tgt[i].score;
        char processed_score_str[4+1] =  {'\0'};
        int str_index = 0;
        while (processing_score > 0)
        {
            processed_score_str[str_index] = (processing_score % 10 + key) % 10 + '0';
            processing_score /= 10;
            ++str_index;
        }
        for (size_t j = 0; j < str_index; j++)
        {
            result[result_index+str_index-j] = processed_score_str[j];
        }
        result_index += str_index;
    }
    result[result_index+1] = '\0';
    return result;
}

char* decrypt(int key, char *str){
    // allocate heap memory to return
    char* result;
    result = (char *)calloc(strlen(str),sizeof(char));

    int i = 0;
    while (str[i] != '\0')
    {
        result[i] = (str[i] - '0' - key + 10) % 10 + '0';
        ++i;
    }
    return result;
}

char* multi(int m){
    // len of result must over 4*DataCount+1
    char* result;
    result = (char *)calloc(DataCount*4+1,sizeof(char));

    // select target array by AlwaysTrySaveSource
    enum ReadyFor *ready_state = NULL;
    struct Student *tgt = NULL;
    getSortedDataById(ready_state,tgt);

    int result_index = 0 - 1;
    for (size_t i = 0; i < DataCount; i++)
    {
        int processing_score = tgt[i].score;
        char processed_score_str[4*2+1] =  {'\0'};
        int str_index = 0;
        while (processing_score > 0)
        {
            // from low digit to top digit
            int num_mutlied = processing_score % 10 * m;
            do
            {
                // 3 digit at most
                processed_score_str[str_index]  = num_mutlied % 10 + '0';
                num_mutlied /= 10;
                ++str_index;
            } while (num_mutlied > 0);
            processing_score /= 10;
        }
        // copy to result array
        for (size_t j = 0; j < str_index; j++)
        {
            result[result_index+str_index-j] = processed_score_str[j];
        }
        result_index += str_index;
    }
    result[result_index+1] = '\0';
    return result;
}

void quickSort(int *arr, int lower, int upper){ // unused
    // Must remember that upper equals index + 1
    long long int datum = arr[lower];
    int datum_index = lower + 1;
    for (size_t i = lower + 1; i < upper; ++i)
    {
        if (datum > arr[i])
        {
            datum = arr[i];
            arr[i] = arr[datum_index];
            arr[datum_index] = datum;
            datum = arr[lower];
            ++datum_index;
        }
    }
    arr[lower] = arr[datum_index-1];
    arr[datum_index-1] = datum;
    if (lower +1 >= upper)
    {
        return;
    }
    quickSort(arr,lower,datum_index);
    quickSort(arr,datum_index,upper);
}

void shellSort(int *arr, int n){ // unused
    // Must remember that upper equals index + 1
    for (size_t gap = n / 2; gap > 0; gap /= 2)
    {
        for (size_t i = 0 ;i < gap; ++i)
        {
            for (size_t j = i + gap; j < n; j += gap)
            {
                if (arr[j] < arr[j - gap])
                {
                    int tmp = arr[j];
                    int k = j - gap;
                    while (k >= 0 && arr[k] > tmp)
                    {
                        arr[k + gap] = arr[k];
                        k -= gap;
                    }
                    arr[k + gap] = tmp;
                }
            }
        }
    }
}

int cmpId(const void *a,const void *b)
{
    struct Student *aa = (struct Student *)a;
    struct Student *bb = (struct Student *)b;
    return (((aa->id) > (bb->id)) ? 1 : -1);
}

int cmpScore(const void *a,const void *b)
{
    struct Student *aa = (struct Student *)a;
    struct Student *bb = (struct Student *)b;
    return (((aa->score) > (bb->score)) ? 1 : -1);
}

int binarySearchId(long long int id, int lower, int upper){
    // I don't use bsearch in stdlib because I want to get index directly
    int mid;
    // searching
    while (lower < upper)
    {
        mid = (lower+upper) / 2;
        if (Data[mid].id > id)
        {
            lower = mid + 1;
        }
        else if (Data[mid].id < id)
        {
            upper = mid;
        }
        else
        {
            return mid;
        }
    }
    // no found
    return -1;
}

int linearSearchId(long long int id, int lower, int upper){
    for (size_t i = lower; i < upper; ++i)
    {
        if (id == Data[i].id)
        {
            return i;
        }
    }
    return -1;
}

void calcRankToCache(){
    for (size_t i = 0; i < DataCount; i++)
    {
        DataCache[i] = Data[i];
    }
    sortDataByScore(DataCache,DataCount);
    DataCacheReady = Rank;
}

int calcRank(enum ExtraBool const_Data, int index_from_Data){
    int tgt_len = DataCount;
    struct Student *tgt = Data;

    // if Data is needed to save original sequece
    if (True == const_Data)
    {
        tgt_len = DataCount;
        tgt = DataCache;
        if (Rank == DataCacheReady)
        {
            return DataCache[index_from_Data].rank;
        }
        else
        {
            sortDataByScore(tgt,tgt_len);
        }
    }

    // False = const_Data here
    // if Data is not sorted for score
    else if (Score != DataReady)
    {
        sortDataByScore(tgt,tgt_len);
    }

    // set rank
    int last_score = -1;
    for (int i = tgt_len - 1; i >= 0; i--)
    {
        if (last_score == tgt[i].score)
        {
            tgt[i].rank = tgt[i+1].rank;
        }
        else
        {
            tgt[i].rank = tgt_len - i;
            last_score = tgt[i].score;
        }

        // if is target id and not calculate all ranks when working on data
        if (True == const_Data && Data[index_from_Data].id == tgt[i].id && False == AlwaysCalculateAllRanksWhenWorkingOnData)
        {
            return tgt_len - i;
        }
    }

    // set status
    if (False == const_Data && True == AlwaysCalculateAllRanksWhenWorkingOnData)
    {
        DataReadyForRank = Rank;
    }

    return Data[index_from_Data].rank;
}

void calcAllRank(){
    if (False == AlwaysTrySaveSource)
    {
        calcRank(AlwaysTrySaveSource, DataCount-1);
    }
    else
    {
        for (size_t i = 0; i < DataCount; i++)
        {
            Data[i].rank = calcRank(AlwaysTrySaveSource,i);
        }
    }
    DataReadyForRank = Rank;
}

void setSettings(){
    int ipt;
    char q = 'q';
    while (0 != ipt)
    {
        printf("Setsettings:\n 1. AlwaysTrySaveSource\n2. AlwaysTryBinarySearch\n3. AlwaysRecalculateBeforeOutput\n4. AlwaysCalculateAllRanksWhenWorkingOnData\n");
        scanf("%d",&ipt);
        switch (ipt)
        {
        case 0:
            break;
        case 1:
            printf("set AlwaysTrySaveSource:\n 1 for False, 2 for True");
            scanf("%d",&ipt);
            if (1 == ipt)
            {
                AlwaysTrySaveSource = False;
            }
            else if (2 == ipt)
            {
                AlwaysTrySaveSource = True;
            }
            else
            {
                AlwaysTrySaveSource = Unset;
                printf("Illegal input");
            }
            break;
        case 2:
            printf("set AlwaysTryBinarySearch:\n 1 for False, 2 for True");
            scanf("%d",&ipt);
            if (1 == ipt)
            {
                AlwaysTryBinarySearch = False;
            }
            else if (2 == ipt)
            {
                AlwaysTryBinarySearch = True;
            }
            else
            {
                AlwaysTryBinarySearch = Unset;
                printf("Illegal input");
            }
            break;
        case 3:
            printf("set AlwaysRecalculateBeforeOutput:\n 1 for False, 2 for True");
            scanf("%d",&ipt);
            if (1 == ipt)
            {
                AlwaysRecalculateBeforeOutput = False;
            }
            else if (2 == ipt)
            {
                AlwaysRecalculateBeforeOutput = True;
            }
            else
            {
                AlwaysRecalculateBeforeOutput = Unset;
                printf("Illegal input");
            }
            break;
        case 4:
            printf("set AlwaysCalculateAllRanksWhenWorkingOnData:\n 1 for False, 2 for True");
            scanf("%d",&ipt);
            if (1 == ipt)
            {
                AlwaysCalculateAllRanksWhenWorkingOnData = False;
            }
            else if (2 == ipt)
            {
                AlwaysCalculateAllRanksWhenWorkingOnData = True;
            }
            else
            {
                AlwaysCalculateAllRanksWhenWorkingOnData = Unset;
                printf("Illegal input");
            }
            break;
        
        default:
            break;
        }
        scanf("%s",ipt);
    }
}

void optMenu(int type){
    if (type == 0)
    {
        printf("Okay, data upload finished. What do you what to do next? You can enter a number to tell me.\n");
    }
    else if (type == 1)
    {
        printf("Do you still need my service? You can enter a number to tell me.\n");
    }
    printf("1 add\n2 adds\n3 delete\n4 search\n5 sort by id\n6 sort by score\n7 best score\n8 worst score\n9 average score\n10 prime judge\n11 coprime judge\n12 encrypt\n13 decrypt\n14 multi\n15 settings\n0 exit\n");
}

void reflashOperateInput(){
    scanf("%d",&OperateInput);
}

void selectCase(){
    long long int n[2];
    switch (OperateInput)
    {
    case 1:
        Add(NULL,-1,-1);
        break;
    case 2:
        scanf("%lld",n);
        Adds(*n,NULL,NULL,NULL);
        break;
    case 3:
        scanf("%lld",n);
        Delete(*n);
        break;
    case 4:
        scanf("%lld",n);
        Search(*n);
        break;
    case 5:
        Sort_by_id();
        break;
    case 6:
        Sort_by_score();
        break;
    case 7:
        printStudent(Max());
        break;
    case 8:
        printStudent(Min());
        break;
    case 9:
        printStudent(Ave());
        break;
    case 10:
        scanf("%lld",n);
        printf(True == prime(*n) ? "score is prime" : "score is not prime");
        break;
    case 11:
        scanf("%lld",&n);
        scanf("%lld",&n+1);
        printf(True == coprime(*n,*(n+1)) ? "score is coprime" : "score is not coprime");
        break;
    case 12:
        scanf("%lld",&n);
        freeer = encrypt(*n);
        printf("%s\n",freeer);
        free(freeer);
        freeer = NULL;
        break;
    case 13:
    {
        scanf("%lld",&n);
        char decrypt_tgt[114514] = {'\0'};
        freeer = decrypt(*n,decrypt_tgt);
        printf("%s\n",freeer);
        free(freeer);
        freeer = NULL;
        break;
    }
    case 14:
        scanf("%lld",&n);
        printf("%s\n",multi(*n));
        break;
    case 15:
        setSettings();
        break;

    case 0:
        exit(0);
        do_pause();
        break;

    default:
        printf("Illegal input!\n");
        break;
    }
    OperateInput = -1;
}

// Syntactic sugars
void Add(char *name, int id, int score){
    appendStudent(1);
}

void Adds(int n, char name[], int id[], int score[]){
    appendStudent(n);
}

void Delete(long long int id){
    deleteStudent(id);
}

void Search(long long int id){
    printStudent(searchStudentById(id));
}

void Sort_by_id(){
    sortDataById(Data,DataCount);
}

void Sort_by_score(){
    sortDataByScore(Data,DataCount);
}

int Max(){
    return findMax();
}

int Min(){
    return findMin();
}

int Ave(){
    return calcAvg();
}


void do_pause(){
    system("pause");
}

int main(){
    printf("Hello, pls input a series of student information!\n");
    int type = 1;
    while (0 != OperateInput)
    {
        optMenu(1 == type ? ++type: type);
        reflashOperateInput();
        selectCase();
    }
    do_pause();
    return 0;
}