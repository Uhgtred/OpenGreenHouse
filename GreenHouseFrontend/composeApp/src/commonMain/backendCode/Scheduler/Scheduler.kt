import java.lang.Runnable
import java.lang.System
import java.util.concurrent.Executors
import java.util.concurrent.TimeUnit


class Scheduler{

    private val scheduler = java.util.concurrent.Executors.newScheduledThreadPool(10)
    private val coroutineDispatcher = scheduler.asCoroutineDispatcher()
    private val scope = CoroutineScope(coroutineDispatcher)
    private var taskList: List = List(10){
        index -> scope.launch{
            while (isActive){
                println("Coroutine $index is running at ${java.lang.System.currentTimeMillis()}")
                taskList[index]()
                delay(60000L)
            }
        }
    }

    fun scheduleRepetitiveTask(task: Runnable, delay: Long){
        /*
        Method for running tasks repetetively.
        */
        scheduler.scheduleAtFixedRate(task, 0, delay, java.util.concurrent.TimeUnit.SECONDS)
    }

}