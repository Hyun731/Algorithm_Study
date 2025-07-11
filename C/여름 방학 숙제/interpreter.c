#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

#define MAX_LINES 100
#define MAX_LINE_LEN 100

typedef struct {
    char name[20];
    int value;
    int is_set;
} Variable;

Variable vars[100];
int var_count = 0;

char* code_lines[MAX_LINES];
int line_count = 0;

Variable* get_var(const char* name) {
    for (int i = 0; i < var_count; i++) {
        if (strcmp(vars[i].name, name) == 0) return &vars[i];
    }
    // 새로 추가
    strcpy(vars[var_count].name, name);
    vars[var_count].is_set = 0;
    return &vars[var_count++];
}

int is_number(const char* str) {
    for (int i = 0; str[i]; i++) {
        if (!isdigit(str[i])) return 0;
    }
    return 1;
}

int eval_expression(const char* left, const char* op, const char* right, int* result) {
    int lhs, rhs;

    // 왼쪽 항
    if (is_number(left)) {
        lhs = atoi(left);
    } else {
        Variable* lvar = get_var(left);
        if (!lvar->is_set) {
            printf("오류: 변수 '%s'가 설정되지 않았습니다.\n", left);
            return 0;
        }
        lhs = lvar->value;
    }

    // 오른쪽 항
    if (is_number(right)) {
        rhs = atoi(right);
    } else {
        Variable* rvar = get_var(right);
        if (!rvar->is_set) {
            printf("오류: 변수 '%s'가 설정되지 않았습니다.\n", right);
            return 0;
        }
        rhs = rvar->value;
    }

    // 연산
    if (strcmp(op, "+") == 0) *result = lhs + rhs;
    else if (strcmp(op, "-") == 0) *result = lhs - rhs;
    else if (strcmp(op, "*") == 0) *result = lhs * rhs;
    else if (strcmp(op, "/") == 0) {
        if (rhs == 0) {
            printf("오류: 0으로 나눌 수 없습니다.\n");
            return 0;
        }
        *result = lhs / rhs;
    } else {
        printf("오류: 지원하지 않는 연산자 '%s'\n", op);
        return 0;
    }

    return 1;
}

void execute_line(const char* line) {
    char cmd[10], arg1[20], arg2[20], arg3[20];

    if (sscanf(line, "%s %s %s %s", cmd, arg1, arg2, arg3) >= 1) {
        if (strcmp(cmd, "print") == 0) {
            Variable* var = get_var(arg1);
            if (!var->is_set) {
                printf("오류: 변수 '%s'가 설정되지 않았습니다.\n", arg1);
                return;
            }
            printf("%s = %d\n", var->name, var->value);
        } else {
            char varname[20];
            strcpy(varname, cmd); // a

            if (strcmp(arg2, "+") == 0 || strcmp(arg2, "-") == 0 ||
                strcmp(arg2, "*") == 0 || strcmp(arg2, "/") == 0) {
                int result;
                if (!eval_expression(arg1, arg2, arg3, &result)) return;
                Variable* var = get_var(varname);
                var->value = result;
                var->is_set = 1;
            } else {
                // 단순 할당: a = b or a = 5
                Variable* var = get_var(varname);
                if (is_number(arg2)) {
                    var->value = atoi(arg2);
                    var->is_set = 1;
                } else {
                    Variable* rhs = get_var(arg2);
                    if (!rhs->is_set) {
                        printf("오류: 변수 '%s'가 설정되지 않았습니다.\n", arg2);
                        return;
                    }
                    var->value = rhs->value;
                    var->is_set = 1;
                }
            }
        }
    }
}

void run_code() {
    for (int i = 0; i < line_count; i++) {
        execute_line(code_lines[i]);
    }
}

int main() {
    char buffer[MAX_LINE_LEN];

    printf("입력하세요. '실행'을 입력하면 실행됩니다.\n");
    while (1) {
        printf("> ");
        fgets(buffer, sizeof(buffer), stdin);
        buffer[strcspn(buffer, "\n")] = 0;

        if (strcmp(buffer, "실행") == 0) {
            run_code();
            break;
        }

        code_lines[line_count++] = strdup(buffer);
    }

    return 0;
}