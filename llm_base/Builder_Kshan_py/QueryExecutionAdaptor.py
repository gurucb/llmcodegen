import SQLExecutor

class QueryExecutionAdapter:
    @staticmethod
    def get_query_executor():
        executor = SQLExecutor()
        return executor
